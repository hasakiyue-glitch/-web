from django.shortcuts import render
from .froms import ResumeForm
# Create your views here.
def contact(request):
    return render(request,'contact.html')
from .models import Ad
def recruit(request):
    AdList = Ad.objects.all().order_by('-publishDate')
    # /*表单*/
    if request.method == 'POST':
        resumeForm = ResumeForm(data=request.POST, files=request.FILES)
        if resumeForm.is_valid():
            resumeForm.save()
            return render(request, 'success.html', {
                'active_menu': 'contactus',
                'sub_menu': 'recruit',
            })
    else:
        resumeForm = ResumeForm()
 # /*表单*/

    return render(
        request, 'recruit.html', {
            'active_menu': 'contactus',
            'sub_menu': 'recruit',
            'AdList': AdList,
            'resumeForm':resumeForm,
        })