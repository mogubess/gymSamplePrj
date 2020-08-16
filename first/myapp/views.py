from django.shortcuts import render


def index(request):
    """マイページの表示制御
    """
    context = {'name': '高田秀昭', 'lastMonth': '7', 'remaining': '3'}
    # DBから引っ張り出す残チケット枚数 今月、先月、先々月
    # 時間情報から現在の月を引っ張る
    # 予約時間が入っているならば、その時間をDBから引っ張り出して、表示する
    # 担当トレーナー、トレーニング場所

    # 一番下に、予約画面に飛ぶボタンを押下
    return render(request, 'myapp/index.html', context=context)


def reserve(request):
    """予約画面の表示制御"""
    traner_list = []
    traner_list.append('井上')
    traner_list.append('佐藤')
    traner_list.append('近藤')

    studio_list = []
    studio_list.append('五反田')
    studio_list.append('品川')
    
    context = {
        'traner_list': traner_list,
        'studio_list': studio_list
    }
    return render(request, 'myapp/reserve.html', context=context)
# from django.http import HttpResponse
# import logging

# logging.basicConfig(level=logging.DEBUG)


# def index(request):
# django.core.handlers.wsgi.WSGIRequest
# logging.critical(request.get_host())
# logging.critical(request.get_full_path())
# logging.critical(request.get_full_path_info(force_append_slash=True))
# logging.critical(request.get_raw_uri())
# return HttpResponse("Hello, world")
