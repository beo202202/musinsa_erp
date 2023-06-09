from django.shortcuts import render, redirect
from .models import AccountsModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model  # 사용자가 데이터베이스 안에 있는지 검사하는 함수
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# 임시 홈


def sign_up(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'accounts/signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        email = request.POST.get('email', '')
        # bio = request.POST.get('bio', '')

        if password != password2:
            # 패스워드가 같지 않다고 알람
            return render(request, 'accounts/signup.html', {'error': '패스워드를 확인 해 주세요!'})
        else:
            if username == '' or password == '':
                return render(request, 'accounts/signup.html', {'error': '사용자 이름과 비밀번호는 필수 값 입니다!'})

            exist_user = get_user_model().objects.filter(username=username)

            if exist_user:
                # 사용자가 존재하기 때문에 사용자를 저장하지 않고 회원가입 페이지를 다시 띄움
                return render(request, 'accounts/signup.html', {'error': '사용자가 존재합니다'})
            else:
                AccountsModel.objects.create_user(
                    username=username, password=password, email=email)  # bio=bio)
                return redirect('/sign-in')

# user = get_user_model().objects.create(username=username).exist():
#     return
# user = get_user_model().objects.create(username=username)
# user.set_password(password)
# user.save()
# return HttpResponse


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        me = auth.authenticate(request, username=username, password=password)
        if me is not None:
            auth.login(request, me)
            return redirect('/')
        else:
            return render(request, 'accounts/login.html', {'error': '유저이름 혹은 패스워드를 확인 해 주세요'})
    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'accounts/login.html')

    # username = request.POST.get("username", "")
    # password = request.POST.get("password", "")

    # user = authenticate(request, username=username, password=password)
    # print(user, type(user))

    # if not user:
    #     return HttpResponse("존재하지 않는 계정이거나 비밀번호가 일치하지 않습니다.")

    # login(request, user)

    # return HttpResponse("")


@login_required
def user_logout(request):
    auth.logout(request)
    return redirect('/')

    # logout(requset)
