from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def count(request):
    full_text = request.GET['fulltext']
    word_list = full_text.split()  # 총 단어수 세는 기능
    word_dictionary = {}

   # 각 단어별로 나온 횟수 세는 기능
    for word in word_list:
        if word in word_dictionary:
            # Increase
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    return render(request, 'count.html', {'fulltext': full_text, 'total': len(word_list), 'dictionary': word_dictionary.items()})
