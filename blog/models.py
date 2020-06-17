from django.db import models
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from wagtail.snippets.models import register_snippet

from wagtail.core.fields import StreamField
from wagtail.core import blocks

from wagtail.images.blocks import ImageChooserBlock

from django.shortcuts import render



class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    def get_context(self, request, *args, **kwargs): #this context has pagination
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        # Get all posts
        all_posts = self.get_children().live().order_by('-first_published_at')
        # Paginate all posts by 6 per page
        paginator = Paginator(all_posts, 5)
        # Try to get the ?page=x value
        page = request.GET.get("page")
        try:
            # If the page exists and the ?page=x is an int
            posts = paginator.page(page)
        except PageNotAnInteger:
            # If the ?page=x is not an int; show the first page
            posts = paginator.page(1)
        except EmptyPage:
            # If the ?page=x is out of range (too high most likely)
            # Then return the last page
            posts = paginator.page(paginator.num_pages)



        # "posts" will have child pages; you'll need to use .specific in the template
        # in order to access child properties, such as youtube_video_id and subtitle
        context["posts"] = posts
        return context


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )


class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)

    body = StreamField([
        ('paragraph', blocks.RichTextBlock()),
        ('html_paragraph', blocks.RawHTMLBlock()),
        ('quote', blocks.BlockQuoteBlock()),
        ('image', ImageChooserBlock()),
    ])


    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    def serve(self, request):
        from .forms import CommentForm
        post = self.blogpage
        comments = post.comments.filter(active=True, parent__isnull=True)
        new_comment = None

        # Comment posted
        if request.method == 'POST':
            comment_form = CommentForm(request.POST)

            if comment_form.is_valid():
                parent_obj = None
                # get parent comment id from hidden input
                try:
                # id integer e.g. 15
                    parent_id = int(request.POST.get('parent_id'))
                except:
                    parent_id = None
                # if parent_id has been submitted get parent_obj id
                if parent_id:
                    parent_obj = Comment.objects.get(id=parent_id)
                # if parent object exist
                    if parent_obj:
                    # create reply comment object
                        reply_comment = comment_form.save(commit=False)
                    # assign parent_obj to reply comment
                        reply_comment.parent = parent_obj
            # normal comment

            # Create Comment object but don't save to database yet
                new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
                new_comment.post_id = self.id
            # Save the comment to the database
                new_comment.save()
                return render(request, self.template, {
                    'page': self,
                    'new_comment': new_comment,
                    'comments': comments,
                    })


        else:
            comment_form = CommentForm()

        return render(request, self.template, {
            'page': self,
            'new_comment': new_comment,
            'comments': comments,
            'comment_form': comment_form,
            })

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
        index.SearchField('tags'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),
        ], heading="Blog information"),
        FieldPanel('intro'),
        StreamFieldPanel('body'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]

class BlogPageGalleryImage(Orderable):
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]


class BlogTagIndexPage(Page):

    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['blogpages'] = blogpages
        return context

@register_snippet
class Comment(models.Model):
    post = models.ForeignKey(BlogPage,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    class Meta:
        ordering = ['created_on']


    def __str__(self):
        if self.active == True:
            return '{} at {} - Published'.format(self.name, str(self.created_on)[0:16])
        else:

            return '{} at {} - Awaiting approval'.format(self.name, str(self.created_on)[0:16])

