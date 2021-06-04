from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
from .models import Player
from .serializers import PlayerSerializer
from django.db.models import Q


@api_view(['POST'])
def createPlayerView(request):
    serializer = PlayerSerializer(data=request.data)
    print("lil yes")
    if serializer.is_valid():
        serializer.save()
        print("yes")
    return Response(serializer.data)

def create_teams(n):
        teams = []
        for i in range(n):
            teams.append([])
        return teams



def fill_Basic(teams):
        keeper_flag,bowler_flag,batters_flag = True,True,True
        keepers = Player.objects.filter(Q(keeper = True))
        bowlers = Player.objects.filter(Q(bowler = True)).order_by("-bowling")
        batters = Player.objects.filter(Q(batsmen = True)).order_by("batting")

        if len(keepers)<len(teams) or len(bowlers)<len(teams) or len(batters)<len(teams):
            return (False,False,False,teams)
        try:
            for i in range(len(teams)):
                teams[i].append(keepers[i].name)
                keepers[i].taken = True
                keepers[i].save()
                
        except:
            keeper_flag = False
        try:       
            for i in range(len(teams)):
                teams[i].append(bowlers[i].name)
                bowlers[i].taken = True
                bowlers[i].save()
                
        except:
            bowler_flag = False
        try:       
            for i in range(len(teams)):
                teams[i].append(batters[i].name)
                batters[i].taken = True
                batters[i].save() 
                   
        except:
            batters_flag = False
        return (keeper_flag,bowler_flag,batters_flag,teams)

def fill_remaining_bowlers(teams):
    remaining_bowlers = Player.objects.filter(
            Q(bowler = True),
            Q(taken = False)
    )
    for i in range(len(remaining_bowlers)):
        if len(teams[i%len(teams)]) < 11:

            teams[i%len(teams)].append(remaining_bowlers[i].name)
            remaining_bowlers[i].taken = True
            remaining_bowlers[i].save()
            i+=1
        else:
            break
    return teams

def fill_remaining_batsmen(teams):
    remaining_batsmen = Player.objects.filter(
            Q(batsmen = True),
            Q(taken = False)
    )
    for i in range(len(remaining_batsmen)):
        if len(teams[i%len(teams)]) < 11:
            teams[i%len(teams)].append(remaining_batsmen[i].name)
            remaining_batsmen[i].taken = True
            remaining_batsmen[i].save()
        else:
            break
    return teams

def reassign_players():
    players = Player.objects.all()
    for player in players:
        player.taken = False
        player.save()

@api_view(['GET'])
def playersView(request):
    player = Player.objects.all()
    serializer = PlayerSerializer(player, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def createTeamView(request,n):
    reassign_players()
    total_players = Player.objects.filter(Q(taken = False))
    if len(total_players) < n * 11:
        return Response("Cannot Form Teams: insufficient PLayers")
    teams = create_teams(n)   
    keeper_flag,bowler_flag,batters_flag,teams = fill_Basic(teams)
    print(teams,"is called")
    print(bowler_flag,batters_flag,keeper_flag)
    if bowler_flag == False or batters_flag == False or keeper_flag == False:
        return Response("Cannot Form Teams: insufficient PLayers")
           
    teams = fill_remaining_bowlers(teams)
    print("after filling bowlers",teams)
    teams = fill_remaining_batsmen(teams)    
    print("after filling batsmen",teams)   
    return Response({"teams":teams})