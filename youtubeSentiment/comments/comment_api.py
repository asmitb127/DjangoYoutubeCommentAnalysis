#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 01:03:14 2018
@author: anshulsaxena
"""
# how to run the file:
#runfile('/Users/anshulsaxena/Dropbox/VOCIQ/api_calls/youtube_video_comments_from_google_api.py', args='OEydHbngSz0', wdir='/Users/anshulsaxena/Dropbox/VOCIQ/api_calls')

# https://developers.google.com/youtube/v3/docs/commentThreads/list
# but that has the client_secrets.json file problem
import sys
import pandas as pd
import time
import numpy as np

from apiclient.discovery import build
from apiclient.errors import HttpError


# arguments to be passed to build function
DEVELOPER_KEY = "AIzaSyDz6pbJER2vUz-_TK-2DGFFrvYXDZcZIb0"
# DEVELOPER_KEY = "AIzaSyCysHF_9nyuiBAM5y7rqw-vn8WKlJupUJw"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# creating youtube resource object for interacting with API
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                developerKey=DEVELOPER_KEY)


# Kind of Global: This list stores the top level comments and their replies here
review_list = []
review_list_headers = ['Video_id', 'Author', 'review',
                       'date']  # to insert this as header of review file
result_list = []
pageToken_list = []
youtube_video_list = []
youtube_video_list_headers = []
dataframe_list = []
dataframe_dict = {"0": "video_list", "1": "comments"}

# for debugging purposes:
search_response_list = []
response_list = []
result_list_replies = []
search_result_list = []
# youtube comments
comment_list = []


# def __init__():
#     pass

# youtube_search method extracts the summary information of the videoId such as like count


def youtube_search(q, max_results=50, order="relevance", token=None, location=None, location_radius=None):
    print("in youtube_search")
    search_response = youtube.search().list(
        q=q,
        type="video",
        pageToken=token,
        order=order,
        part="id,snippet",  # Part signifies the different kinds of data you want
        maxResults=max_results,
        location=location,
        locationRadius=location_radius).execute()
    print(search_response)

    search_response_list.append(search_response)

    channelId = []
    channelTitle = []
    categoryId = []
    viewCount = []
    likeCount = []
    dislikeCount = []
    commentCount = []
    favoriteCount = []
    category = []
    tags = []
    videos = []

    for search_result in search_response.get("items", []):

        # just for debugging:
        search_result_list.append(search_result)

        if search_result["id"]["kind"] == "youtube#video":
            youtube_video_list_headers.append('title')
            title = search_result['snippet']['title']

            youtube_video_list_headers.append('videoId')
            videoId = search_result['id']['videoId']

            response = youtube.videos().list(
                part='statistics,snippet',
                id=search_result['id']['videoId']).execute()

            response_list.append(response)

            youtube_video_list_headers.append('channelId')
            channelId = response['items'][0]['snippet']['channelId']

            youtube_video_list_headers.append('channelTitle')
            channelTitle = response['items'][0]['snippet']['channelTitle']

            youtube_video_list_headers.append('categoryId')
            categoryId = response['items'][0]['snippet']['categoryId']

            youtube_video_list_headers.append('favoriteCount')
            favoriteCount = response['items'][0]['statistics']['favoriteCount']

            youtube_video_list_headers.append('viewCount')
            viewCount = response['items'][0]['statistics']['viewCount']

            youtube_video_list_headers.append('likeCount')
            likeCount = response['items'][0]['statistics']['likeCount']

            youtube_video_list_headers.append('dislikeCount')
            dislikeCount = response['items'][0]['statistics']['dislikeCount']

        #youtube_dict = {'tags':tags,'channelId': channelId,'channelTitle': channelTitle,'categoryId':categoryId,'title':title,'videoId':videoId,'viewCount':viewCount,'likeCount':likeCount,'dislikeCount':dislikeCount,'commentCount':commentCount,'favoriteCount':favoriteCount}
        youtube_video_list.append([title, videoId, channelId, channelTitle,
                                   categoryId, favoriteCount, viewCount, likeCount, dislikeCount])
        # df1 = pd.DataFrame.from_records(
        #     youtube_video_list, columns=youtube_video_list_headers)
        # dataframe_list.append(df1)
        break


# Call the API's commentThreads.list method to list the existing comment threads.
def get_comment_threads(video_id, nextPageToken=""):
    print("in get_comment_threads")
    pageToken_list.append(nextPageToken)
    results = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        textFormat="plainText",
        maxResults=100, pageToken=nextPageToken
    ).execute()

    result_list.append(results)

    for item in results["items"]:
        comment = item["snippet"]["topLevelComment"]
        author = comment["snippet"]["authorDisplayName"]
        text = comment["snippet"]["textDisplay"]
        date = comment["snippet"]["updatedAt"][:10]
        date = date[8:10]+"/"+date[5:7]+"/"+date[:4]
        review_list.append([video_id, author, text, date])
        # print(comment["snippet"]["textDisplay"])
        comment_list.append([text, author])

    if "nextPageToken" in results:
        print("nextPage exists")
        get_comment_threads(video_id, results["nextPageToken"])
        return 1
    print("end of get_comment_threads")
    # clean_comments.slice_comments(comment_list)
    # print(clean_comments.sorted_lest_freq)
    # print(clean_comments.sorted_most_freq)
    # return comment_list
    # return results["items"]
