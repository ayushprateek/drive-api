from rest_framework.views import APIView
from rest_framework.response import Response
from apps.user.models import UserPlanTripLogs
from django.db.models import Count, F
from django.db.models import Avg
from django.db.models.functions import TruncHour, TruncDate, TruncWeek, TruncMonth
from datetime import datetime
import json

class TopSearchedRoutesView(APIView):
    """
    API view to fetch the top searched routes based on origin and destination.

    Returns the top 5 searched routes with the highest search counts.
    """
    def get(self, request):
        try:
            start_date = ""
            end_date = ""
            if request.GET.items():
                for item, val in request.GET.items():
                    date_obj = json.loads(item)
                    if date_obj.get("start_date"):
                        start_date = date_obj.get("start_date", None)
                    if date_obj.get("end_date"):
                        end_date = date_obj.get("end_date", None)

                # Convert string dates to datetime objects
                if start_date and end_date:
                    start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
                    end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
                    top_routes = UserPlanTripLogs.objects.filter(created_at__range=(start_date, end_date)
                                                                ).values('origin', 'destination'
                                                                            ).annotate(count=Count('id')
                                                                                    ).order_by('-count')[:5]
                
                else:
                    top_routes = UserPlanTripLogs.objects.values('origin', 'destination').annotate(count=Count('id')).order_by(
                        '-count')[:5]
                return Response(top_routes)
        except Exception as e:
            return Response({"error": str(e)}, status=400)


class TopUsersView(APIView):
    """
    API view to fetch the top users with the highest number of searches.

    Returns the top 5 users with the highest search counts.
    """
    def get(self, request):
        try:
            start_date = ""
            end_date = ""
            if request.GET.items():
                for item, val in request.GET.items():
                    date_obj = json.loads(item)
                    if date_obj.get("start_date"):
                        start_date = date_obj.get("start_date", None)
                    if date_obj.get("end_date"):
                        end_date = date_obj.get("end_date", None)

                # Convert string dates to datetime objects
                if start_date and end_date:
                    start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
                    end_date = datetime.strptime(end_date, '%Y-%m-%d').date()

                    top_users = UserPlanTripLogs.objects.filter(created_at__range=(start_date, end_date)
                                                                ).values('user__first_name', "user__email").annotate(
                        count=Count('id')).order_by('-count')[:5]
                else:
                    top_users = UserPlanTripLogs.objects.values('user__first_name', "user__email").annotate(
                    count=Count('id')).order_by('-count')[:5]
            return Response(top_users)
        except Exception as e:
            return Response({"error": str(e)}, status=400)


class SearchTimeAnalysisView(APIView):
    """
    API view to analyze search times, including average response time and busiest hours for searches.
    """
    def get(self, request):
        try:
            start_date = ""
            end_date = ""
            if request.GET.items():
                for item, val in request.GET.items():
                    date_obj = json.loads(item)
                    if date_obj.get("start_date"):
                        start_date = date_obj.get("start_date", None)
                    if date_obj.get("end_date"):
                        end_date = date_obj.get("end_date", None)

                # Convert string dates to datetime objects
                if start_date and end_date:
                    start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
                    end_date = datetime.strptime(end_date, '%Y-%m-%d').date()

                    # Calculate the average time taken for searches
                    avg_search_time = UserPlanTripLogs.objects.filter(created_at__range=(start_date, end_date)).aggregate(avg_time=Avg('response_time'))['avg_time']

                    # Calculate the busiest hours for searches
                    busiest_hours = UserPlanTripLogs.objects.filter(created_at__range=(start_date, end_date)).annotate(hour=TruncHour('route_request_timestamp')).values(
                        'hour').annotate(count=Count('id')).order_by('-count')[:5]

                else:

                    # Calculate the average time taken for searches
                    avg_search_time = UserPlanTripLogs.objects.aggregate(avg_time=Avg('response_time'))['avg_time']

                    # Calculate the busiest hours for searches
                    busiest_hours = UserPlanTripLogs.objects.annotate(hour=TruncHour('route_request_timestamp')).values(
                        'hour').annotate(count=Count('id')).order_by('-count')[:5]

            return Response({
                "average_search_time": round(avg_search_time, 4),
                "busiest_hours": busiest_hours
            })
        except Exception as e:
            return Response({"error": str(e)}, status=400)


class UserBehaviorAnalyticsView(APIView):
    """
    API view to analyze user behavior, including user retention and engagement.
    """
    def get(self, request):
        try:
            start_date = ""
            end_date = ""
            if request.GET.items():
                for item, val in request.GET.items():
                    date_obj = json.loads(item)
                    if date_obj.get("start_date"):
                        start_date = date_obj.get("start_date", None)
                    if date_obj.get("end_date"):
                        end_date = date_obj.get("end_date", None)

                # Convert string dates to datetime objects
                if start_date and end_date:
                    start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
                    end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
                    # User retention analysis
                    user_retention = UserPlanTripLogs.objects.filter(created_at__range=(start_date, end_date)
                                                            ).values('user__first_name', "user__email").annotate(
                        total_searches=Count('id'),
                        last_search=F('route_request_timestamp'),
                    ).order_by('-last_search')

                    # User engagement analysis
                    user_engagement = UserPlanTripLogs.objects.filter(created_at__range=(start_date, end_date)
                                                            ).values('user__first_name', "user__email").annotate(
                        total_searches=Count('id'),
                    ).order_by('-total_searches')

                else:
                    # User retention analysis
                    user_retention = UserPlanTripLogs.objects.values('user__first_name', "user__email").annotate(
                        total_searches=Count('id'),
                        last_search=F('route_request_timestamp'),
                    ).order_by('-last_search')

                    # User engagement analysis
                    user_engagement = UserPlanTripLogs.objects.values('user__first_name', "user__email").annotate(
                        total_searches=Count('id'),
                    ).order_by('-total_searches')
            return Response({
                "user_retention": user_retention,
                "user_engagement": user_engagement
            })
        except Exception as e:
            return Response({"error": str(e)}, status=400)


class TopSearchedCategories(APIView):
    """
    API view to fetch the top searched categories across all users.

    Returns the top 10 searched categories and their search counts.
    """
    def get(self, request):
        try:
            start_date = ""
            end_date = ""
            if request.GET.items():
                for item, val in request.GET.items():
                    date_obj = json.loads(item)
                    if date_obj.get("start_date"):
                        start_date = date_obj.get("start_date", None)
                    if date_obj.get("end_date"):
                        end_date = date_obj.get("end_date", None)

                # Convert string dates to datetime objects
                if start_date and end_date:
                    start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
                    end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
                

                    # Query to get the top searched categories and their counts across all users
                    top_searched_categories = UserPlanTripLogs.objects.filter(created_at__range=(start_date, end_date)
                                                            ).values_list('categories', flat=True)

                    # Flatten the list of category arrays
                    all_categories = [category for categories in top_searched_categories for category in categories]
                else:

                    # Query to get the top searched categories and their counts across all users
                    top_searched_categories = UserPlanTripLogs.objects.values_list('categories', flat=True)

                    # Flatten the list of category arrays
                    all_categories = [category for categories in top_searched_categories for category in categories]

            # Calculate the count of each category
            category_counts = {}
            for category in all_categories:
                if category in category_counts:
                    category_counts[category] += 1
                else:
                    category_counts[category] = 1

            # Sort categories by count and get the top 10
            top_categories = dict(sorted(category_counts.items(), key=lambda item: item[1], reverse=True)[:10])

            return Response(top_categories)
        except Exception as e:
            return Response({"error": str(e)}, status=400)


class AnalyticsDataView(APIView):
    """
    API view to retrieve analytics data based on specified type and date range.

    You can request custom, day, week, or month analytics data. For custom range, specify start_date and end_date.
    """
    def get(self, request):
        analytics_type = request.query_params.get('type')  # Type of analytics (e.g., custom, day, week, month)
        try:
            start_date = ""
            end_date = ""
            if analytics_type == "custom":
                for item, val in request.GET.items():
                    date_obj = json.loads(item)
                    if date_obj.get("start_date"):
                        start_date = date_obj.get("start_date", None)
                    if date_obj.get("end_date"):
                        end_date = date_obj.get("end_date", None)

                # Convert string dates to datetime objects
                if start_date and end_date:
                    start_date = datetime.strptime(start_date, '%Y-%m-%d')
                    end_date = datetime.strptime(end_date, '%Y-%m-%d')

                    # Fetch searches within the specified date range
                    searches = UserPlanTripLogs.objects.filter(route_request_timestamp__range=(
                        start_date, end_date)).annotate(
                            date=TruncDate('route_request_timestamp')).values('date').annotate(count=Count('id'))

                if not start_date or not end_date:
                    return Response({"error": "Custom date range requires start_date and end_date."}, status=400)

            elif analytics_type == 'day':
                searches = UserPlanTripLogs.objects.annotate(date=TruncDate('route_request_timestamp')).values('date').annotate(count=Count('id'))

            elif analytics_type == 'week':
                searches = UserPlanTripLogs.objects.annotate(week=TruncWeek('route_request_timestamp')).values('week').annotate(count=Count('id'))

            elif analytics_type == 'month':
                searches = UserPlanTripLogs.objects.annotate(month=TruncMonth('route_request_timestamp')).values('month').annotate(count=Count('id'))

            else:
                return Response({"error": "Invalid analytics type."}, status=400)

            return Response(searches)   
        except Exception as e:
            return Response({"error": str(e)}, status=400)

