from django.shortcuts import render
from comments.models import Comments, Videos
from django.http import request, HttpResponse, JsonResponse
# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


from comments.models import Videos, Comments, Author, Channel

from . import clean_comments
from . import comment_api
from . import Words
from . import serializers


@api_view(['POST'])
def processUrl(request):

    if request.method == 'POST':
        # cleaning all data before again using it
        comment_api.comment_list.clear()
        clean_comments.dictionay.clear()
        clean_comments.sorted_most_freq.clear()
        clean_comments.sorted_lest_freq.clear()
        # getting the posted url request
        url = request.data["videourl"]
        videoid = url.replace('https://www.youtube.com/watch?v=', '')
        comment_api.youtube_search(videoid)
        comment_api.get_comment_threads(videoid)
        video_comment_threads = comment_api.comment_list
        # print(video_comment_threads)
        # adding data to django database
        # channel = Channel(
        #     channel_name=comment_api.youtube_video_list[0][3], channel_id=comment_api.youtube_video_list[0][2])
        # channel.save()
        channel = Channel.objects.get_or_create(
            channel_name=comment_api.youtube_video_list[0][3], channel_id=comment_api.youtube_video_list[0][2])
        # channel.save()
        videoItem = Videos(likes=comment_api.youtube_video_list[0][7], dislikes=comment_api.youtube_video_list[0][8],
                           channel=channel[0], title=comment_api.youtube_video_list[0][0])
        videoItem.save()
        comments = []
        for item in video_comment_threads:
            author_name = item[1]
            author = Author.objects.get_or_create(name=author_name)
            # author.save()
            text = item[0]
            comment = Comments(author=author[0], video=videoItem, comment=text)
            comment.save()
            comments.append(text)
        # for analysis
        clean_comments.slice_comments(comments)
        # least frequent--followed by----most frequent------------
        least_and_most_words = []
        # most_words = []
        for value in clean_comments.get_least_frequent():
            word = Words.Words(value[0], value[1])
            least_and_most_words.append(word)
        for value in clean_comments.get_most_frequent():
            word = Words.Words(value[0], value[1])
            least_and_most_words.append(word)
        serialData = serializers.WordsSerializer(
            least_and_most_words, many=True)

        return JsonResponse(serialData.data, safe=False)

    return Response(status=status.HTTP_400_BAD_REQUEST)
