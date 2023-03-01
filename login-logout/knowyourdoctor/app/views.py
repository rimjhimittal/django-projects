from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your passwords do not match")
        else:
            my_user= User.objects.create_user(uname, email, pass1)
            my_user.save()
        return redirect('login')

    return render(request, 'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username and password do not match")
    return render(request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')


# def extract_text(file):
#     # Extracts text from either an image or PDF file
#     text = ''
#     if file.content_type == 'image/jpeg' or file.content_type == 'image/png':
#         img = Image.open(io.BytesIO(file.read()))
#         text = pytesseract.image_to_string(img)
#     elif file.content_type == 'application/pdf':
#         pdf_reader = PyPDF2.PdfFileReader(io.BytesIO(file.read()))
#         for page in range(pdf_reader.getNumPages()):
#             text += pdf_reader.getPage(page).extractText()
#     return text

# def upload_file(request):
#     if request.method == 'POST':
#         form = FileUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             text = extract_text(request.FILES['file'])
#             return render(request, 'result.html', {'text': text})
#     else:
#         form = FileUploadForm()
#     return render(request, 'upload.html', {'form': form})