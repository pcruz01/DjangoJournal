from django.urls import path
from .views import indexPageView, aboutPageView, genConfPageView, stakeConfPageView, churchPageView, byuPageView, missionPageView

urlpatterns = [
    path("mission/", missionPageView, name="mission"),
    path("byu/", byuPageView, name="byu"),
    path("church/", churchPageView, name="church"),
    path("stake_conf/", stakeConfPageView, name="stakeConf"),
    path("gen_conf/", genConfPageView, name="genConf"),
    path("about/", aboutPageView, name="about"),
    path("", indexPageView, name="index")
]
