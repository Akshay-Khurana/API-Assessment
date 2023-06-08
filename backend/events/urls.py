from rest_framework import routers

from events.views import EventAPIViewset

router = routers.SimpleRouter()
router.register('', EventAPIViewset, basename='event-api')

urlpatterns = router.urls
