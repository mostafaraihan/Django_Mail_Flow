from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.timezone import now

def signup_view(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        email = request.POST.get("email")

        # Email context
        context = {
            "site_name": "Raihan World",
            "user": {"first_name": first_name},
            "current_year": now().year,
        }

        # Render email template
        html_content = render_to_string("massage.html", context)

        # Send email
        email_message = EmailMultiAlternatives(
            subject="Welcome to Raihan World!",
            body="Welcome to Raihan World!",
            from_email="Raihan World <noreply@raihanworld.com>",
            to=[email],
        )
        email_message.attach_alternative(html_content, "text/html")
        email_message.send()

        # Redirect to GET page with query param
        return redirect('/?success=1')

    # GET request
    success = request.GET.get('success')
    return render(request, "form.html", {
        "message": "Welcome email sent successfully!" if success else None
    })
