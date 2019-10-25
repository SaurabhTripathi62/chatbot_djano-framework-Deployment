from django.shortcuts import render
# Create your views here.
import json
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import JsonResponse
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from chatterbot.trainers import ChatterBotCorpusTrainer
from django.contrib.auth.models import AbstractUser
from rest_framework.views import APIView #APIView
from .apps import ChatAppConfig
from rest_framework.response import Response
import re

#from chatterbot.ext.django_chatterbot.models import Conversation,Response#added on debug
#from chatterbot.conversation import Statement
from chatterbot.conversation import Statement
from chatterbot.trainers import ListTrainer # for list part

class ChatterBotAppView(TemplateView):
    template_name = 'app.html'
    
    

class ChatterBotApiView(APIView):
    """
    Provide an API endpoint to interact with ChatterBot.
    """
#trainer = ChatterBotCorpusTrainer(chatbot10) 

    
    chatterbot = ChatBot(**settings.CHATTERBOT)
    #'''
    path_AI_Praadis=r'E:\stwork\subjective questions all for chatbot\notepad files\AI_Pradiss_chat.txt'
    AI_Praadis=open(path_AI_Praadis).read().split('\n')

    trainer=ListTrainer(chatterbot)
    trainer.train(AI_Praadis)#list of basic dilouges
    #'''
    trainer = ChatterBotCorpusTrainer(chatterbot) #added
    trainer.train(*settings.CHATTERBOT['training_data'])
    
    #'trainer': 'chatterbot.trainers.ChatterBotCorpusTrainer',
    #'training_data': [
        
    '''              #*settings.CHATTERBOT,
                  "chatterbot.corpus.english.sports",
                  "chatterbot.corpus.english.science",
                  "chatterbot.corpus.english.movies",
                  "chatterbot.corpus.english.humor",
                  "chatterbot.corpus.english.health",
                  "chatterbot.corpus.english.greetings",
                  "chatterbot.corpus.english.food",
                  "chatterbot.corpus.english.emotion",
                  "chatterbot.corpus.english.conversations",
                  "chatterbot.corpus.english.computers",
                  "chatterbot.corpus.english.botprofile"
                  
                 )
    '''
   #==============>
    def post(self, request, *args, **kwargs):
                """
                Return a response to the statement in the posted data.
                * The JSON data should contain a 'text' attribute.
                """
                input_data = json.loads(request.body.decode('utf-8'))

                if 'text' not in input_data:
                    return JsonResponse({
                        'text': [
                            'The attribute "text" is required.'
                        ]
                    }, status=400)

                while True:
                    userInput=input_data["text"]
                    userInput=userInput.lower()
                    userInput=re.sub(r"[+]"," + ",userInput)
                    userInput=re.sub(r"[-]"," - ",userInput)
                    userInput=re.sub(r"[/]"," / ",userInput)
                    userInput=re.sub(r"[*]"," * ",userInput)
                    userInput=re.sub(r"[%]"," % ",userInput)
                    userInput=re.sub(r"\["," ( ",userInput)
                    userInput=re.sub(r"\]"," ) ",userInput)
                    userInput=re.sub(r"\{"," ( ",userInput)
                    userInput=re.sub(r"\}"," ) ",userInput)
                    userInput=re.sub(r" u " ,"you",userInput)
                    userInput=re.sub(r" r " ,"are",userInput)

                    if userInput=="bye":
                        msgstr='(@@,) Nice Talking to you,see you next time (^,^) ... Good Day! (",) '
                        break 
                    elif userInput!="":
                        msgstr= self.chatterbot.get_response(userInput)
                    else:
                        msgstr='"I dont understand that one !", type "bye" if you want to leave'

                    #response=#added 21oct
                    #response = self.chatterbot.get_response(input_data)
                    response_data={}
                    response_data = msgstr.serialize()#what does this step do ?
                    reply={}
                    reply["text"] = response_data["text"]
                    return JsonResponse(reply, status=200)
                    
    def get(self, request, *args, **kwargs):
                    """
                    Return data corresponding to the current conversation.
                    """
                    return JsonResponse({
                        'name': self.chatterbot.name
                    })



#=================
'''
    def post(self, request, *args, **kwargs):
        """
        Return a response to the statement in the posted data.
        * The JSON data should contain a 'text' attribute.
        """
        input_data = json.loads(request.body.decode('utf-8'))

        if 'text' not in input_data:
            return JsonResponse({
                'text': [
                    'The attribute "text" is required.'
                ]
            }, status=400)

        #response=#added 21oct
        response={}
        response["text"] = self.chatterbot.get_response(input_data)
        #response_data = response.serialize()
        print(response)
            #response=ChatAppConfig.chatbot(input_data)
        #return JsonResponse(response, status=200)
        return Response(response)
        
        
    def get(self, request, *args, **kwargs):
        """
        Return data corresponding to the current conversation.
        """
        return JsonResponse({
            'name': self.chatterbot.name
        })
        
    '''