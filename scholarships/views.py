from django.shortcuts import render
from scholarships.models import Scholarship

# Create your views here.
    def like_scholarship(request, scholarship_id):
        scholarship = get_object_or_404(Scholarship, id=scholarship_id)
        user = request.user  # Assuming you have authentication and user context

        scholarship.increment_likes(user)