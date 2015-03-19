from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from ..user.models import User
from .form import UserFileForm
from .models import UserFile


def user_files(request, pk):
    user = User.objects.get(pk=pk)
    form = UserFileForm

    if request.method == 'POST':
        form = UserFileForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.user = user
            form.save()

    files = UserFile.objects.filter(user=user)

    return render(request, 'files/files.html',
                  {
                      'user': user,
                      'form': form,
                      'files': files,

                  })


#@require_POST
def delete(request, pk, user_id):
    user = User.objects.get(pk=user_id)
    userfile = UserFile.objects.get(pk=pk)

    if userfile.user == user:
        userfile.delete()
        return redirect('/files/' + user_id + '/')
    else:
        return render(request, 'error/forbidden.html')