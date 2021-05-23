from django.db.models.signals import m2m_changed, post_save
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.dispatch import receiver
from .models import Post

#models
from .models import Post


@receiver(m2m_changed, sender = Post.category.through)
def notifyUsers(sender, instance, **kwargs):
    post_info = instance.category.all()
    for category in post_info:

        if category.subscribers:

            for user in category.subscribers.all():
                html_content = render_to_string(
                    'newPublication.html',
                    {
                        'category_info': category,
                        'post_id' : instance.id,
                        'user' : user
                    }
                )
            
                msg = EmailMultiAlternatives(
                    subject = f'{instance.post_title}',
                    body = f'Hello {user.username} we invite you to read a new Post in your prefer category {category}',
                    from_email = 'artiom199821zxc@gmail.com',
                    to = [f'{user.email}']
                )
                msg.attach_alternative(html_content, "text/html")

                msg.send()