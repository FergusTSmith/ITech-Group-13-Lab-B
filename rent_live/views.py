from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.edit import DeleteView
from rent_live.models import Category, LettingAgent, City, Rental_Property, User, PropertyComment, UserProfile, UserMessage, AgentComment
from rent_live.forms import UserForm, UserProfileForm, AgentProfileForm, ProfileEditForm, RentalPropertyForm, UserMessageForm, RentalPropertyComment, LettingAgentComment
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout


# Create your views here.
class IndexView(View):
    def get(self, request):
        property_list = Rental_Property.objects.order_by('-followers')[:3]
        lettingagent_list = LettingAgent.objects.order_by('-qualityRating')[:3]
        city_list = City.objects.order_by('name')
        all_properties = Rental_Property.objects.order_by('followers')
        numberOfProperties = 0

        for i in all_properties:
            numberOfProperties = numberOfProperties+1

        context_dict = {}
        context_dict['properties'] = property_list
        context_dict['lettingAgents'] = lettingagent_list
        context_dict['city'] = city_list
        context_dict['numberOfProperties'] = numberOfProperties

        response = render(request, 'rent_live/index.html', context=context_dict)

        return response



class rating(View):
    def post(self, request):
        print(request.user)
        type_ = request.POST.get("type")
        star_num = request.POST.get("_")
        user = request.POST.get("user")
        print(type_,star_num,user)
        print(request.POST.get("agent_name"),"2"*50)
        a_ = LettingAgent.objects.get(slug = str(request.POST.get("agent_name")))
        print(1)
        if type_ =="help":
            try:
                print(1)
                print(a_.like_help_jsons,user)
                if str(user) in eval(a_.like_help_jsons)[0]:
                    print(2)

                    return HttpResponse("already rated")
            except:
                pass

            if a_.like_help_jsons =="":

                print(3)

                a_.like_help_jsons =  str([{user:star_num}])
                a_.save()

                print(a_.like_help_jsons)
            else:
                print(a_.like_help_jsons)
                print(4)

                try:
                    last= eval(a_.like_help_jsons)[0].append({user:star_num})
                    print(last)
                    a_.like_help_jsons = str(eval(a_.like_help_jsons).append({user:star_num}))
                except:
                    a_.like_help_jsons =  str([{user:star_num}])
                a_.save()

            return HttpResponse("rate success")

        if type_ =="quality":
            try:
                print(1)
                print(a_.like_quality_jsons,user)
                if str(user) in eval(a_.like_quality_jsons)[0]:
                    print(2)

                    return HttpResponse("already rated")
            except:
                pass

            if a_.like_quality_jsons =="":

                print(3)

                a_.like_quality_jsons =  str([{user:star_num}])
                a_.save()

                print(a_.like_quality_jsons)
            else:
                print(a_.like_quality_jsons)
                print(4)

                try:
                    last= eval(a_.like_quality_jsons)[0].append({user:star_num})
                    print(last)
                    a_.like_quality_jsons = str(eval(a_.like_quality_jsons).append({user:star_num}))
                except:
                    a_.like_quality_jsons =  str([{user:star_num}])
                a_.save()

            return HttpResponse("rate success")



        registered = False
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'ProfilePic' in request.FILES:
                profile.profilePic = request.FILES['ProfilePic']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)

class AboutView(View):
    def get(self, request):
        response = render(request, 'rent_live/about.html', context={})
        return response



class serachData(View):
    def get(self, request):
        print(123123)
        return HttpResponse({"ss":9})



class ContactView(View):
    def get(self, request):
        response = render(request, 'rent_live/contact.html', context={})
        return response

class SearchView(View):
    def get(self, request):
        response = render(request, 'rent_live/search.html', context={})
        return response

#https://learndjango.com/tutorials/django-search-tutorial
class SearchResultView(View):
    def getQuery(self, request):
        query = self.request.GET.get('search')
        print(query)
        try:
            city = City.objects.get(name=query)
            result_list = Rental_Property.objects.filter(city = city)
        except City.DoesNotExist:
            result_list = None
        return result_list
    
    def get(self, request):
        context_dict = {}
        model = Rental_Property
        result_list = self.getQuery(request)
        context_dict['results'] = result_list

        response = render(request, 'rent_live/searchresult.html', context=context_dict)
        return response


# https://learndjango.com/tutorials/django-search-tutorial
class SearchResultView1(View):
    def getQuery(self, request):
        query = self.request.GET.get('search')
        print(query)
        try:
            city = City.objects.get(name=query)
            result_list = Rental_Property.objects.filter(city=city)
            mydate = []
            for item in result_list:
                mydate.append(item.lettingAgent)
        except City.DoesNotExist:
            result_list = None
        return mydate

    def get(self, request):
        context_dict = {}
        model = Rental_Property
        result_list = self.getQuery(request)
        context_dict['results'] = result_list

        response = render(request, 'rent_live/searchresult1.html', context=context_dict)
        return response
class CityView(View):
    def get_city_details(self, cityname):
        context_dict = {}

        try:
            city = City.objects.get(slug=cityname)
            rental_properties = Rental_Property.objects.filter(city=city)
            agents = LettingAgent.objects.filter(city=city)

            context_dict['city'] = city
            context_dict['properties'] = rental_properties
            context_dict['agents'] = agents
      
        except City.DoesNotExist:
            context_dict['city'] = None
            context_dict['properties'] = None
            context_dict['agents'] = None
        

        return context_dict

    
    def get(self, request, cityname):
        context_dict = self.get_city_details(cityname)
        
        response = render(request, 'rent_live/city.html', context=context_dict)
        return response


class Rental_PropertyView(View):
    def get_rental_property(self, rental_property_name_slug):
        context_dict = {}

        try:
            rental_property = Rental_Property.objects.get(slug=rental_property_name_slug)
            #agents = LettingAgent.objects.get(name=rental_property)

            context_dict['property'] = rental_property
        except Rental_Property.DoesNotExist:
            context_dict['property'] = None
        
        return context_dict
   
    def get(self, request, rental_property_name_slug):
        context_dict = self.get_rental_property(rental_property_name_slug)
        user = request.user
        is_followed = False
        try:
            rental_property = Rental_Property.objects.get(slug=rental_property_name_slug)
            followers = rental_property.followingUsers.all()
            comments = PropertyComment.objects.filter(property=rental_property)

            for i in followers:
                if i == user:
                    is_followed=True

            for i in comments:
                liking_users = i.likingUsers.all()
                for j in liking_users:
                    if j == user:
                        i.userHasNotLiked = False

            context_dict['isFollowed'] = is_followed
            context_dict['comments'] = comments
        except Rental_Property.DoesNotExist:
            context_dict['isFollowed'] = None
            context_dict['comments'] - None

        response = render(request, 'rent_live/rentalproperty.html', context=context_dict)
        return response

class LettingAgentView(View):
    def get_agent(self, request, letting_agent_name_slug):
        context_dict = {}
        user=request.user

        try:
            letting_agent = LettingAgent.objects.get(slug=letting_agent_name_slug)
            # print(letting_agent.like_help_jsons,letting_agent.like_help_jsons,"*"*200)
            properties = Rental_Property.objects.filter(lettingAgent=letting_agent)
            comments = AgentComment.objects.filter(agent=letting_agent)
            context_dict['comments'] = comments

            for i in comments:
                liking_users = i.likingUsers.all()
                for j in liking_users:
                    if j == user:
                        i.userHasNotLiked = False

            try:
                help_ = str(letting_agent.like_help_jsons)
                help_num = eval(help_)[0]
                total = 0
                for i in help_num:
                    total += int(help_num[i])
                help_average = total/len(help_num)

                context_dict["help_num"] = len(help_num)
                context_dict["help_ave"] = help_average


                quality_ = str(letting_agent.like_quality_jsons)
                quality_num = eval(quality_)[0]
                total = 0
                for i in quality_num:
                    total += int(quality_num[i])
                quality_average = total/len(quality_num)
                context_dict["quality_num"] = len(quality_num)
                context_dict["quality_ave"] = quality_average
            except:
                try:
                    context_dict["help_num"] = len(help_num)
                    context_dict["help_ave"] = help_average
                    context_dict["quality_num"] = len(quality_num)
                    context_dict["quality_ave"] = quality_average
                except:
                    letting_agent.like_help_jsons=""
                    letting_agent.like_quality_jsons=""
                    context_dict["help_num"] = 0
                    context_dict["help_ave"] = 0
                    context_dict["quality_num"] = 0
                    context_dict["quality_ave"] = 0
            context_dict['agent'] = letting_agent
            context_dict['properties'] = properties
        except LettingAgent.DoesNotExist:
            context_dict['agent'] = None
            
        
        return context_dict
   
    def get(self, request, letting_agent_name_slug):


        context_dict = self.get_agent(request, letting_agent_name_slug)
        print(request.user,"pppppppppppp")
        if str(request.user) != "AnonymousUser":
            context_dict["login"] = "1"
            print(context_dict)
            print("{} login".format(request.user))

        else:
            try:
                context_dict.pop("login")
            except:
                pass
            print("{} no login".format(request.user))
            print(context_dict)
        
        return render(request, 'rent_live/lettingagentpage.html', context=context_dict)

class LACommentsView(View):
    def get(self, request):
        return HttpResponse("This is the page detailing the comments for letting agent")

class LAPropertiesView(View):
    def get(self, request):
        return HttpResponse("This is the page for seeing specific rental properties offered by a letting agent")

class RegisterView(View):    
    def get(self, request):
        registered = False
        user_form = UserForm()
        profile_form = UserProfileForm()
        
        response = render(request, 'rent_live/register.html', context={'user_form': user_form, 'profile_form': profile_form, 'registered': registered})
        return response
    
    def post(self, request):
        registered = False
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'ProfilePic' in request.FILES:
                profile.profilePic = request.FILES['ProfilePic']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)

        response = render(request, 'rent_live/register.html', context={'user_form': user_form, 'profile_form':profile_form,'registered':registered})
        return response

class LettingAgentRegisterView(View):
    def get(self, request):
        registered = False
        agent_form = AgentProfileForm()
        user_form = UserForm()

        response = render(request, 'rent_live/lettingagentregister.html', context={'agent_form': agent_form, 'user_form': user_form, 'registered': registered})
        return response

    def post(self, request):
        registered = False
        user_form = UserForm(request.POST)
        agent_form = AgentProfileForm(request.POST)

        if user_form.is_valid() and agent_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            agent = agent_form.save(commit=False)
            agent.user = user

            if 'logo' in request.FILES:
                agent.logo = request.FILES['logo']
            
            agent.save()
            registered = True
        else:
            print(user_form.errors, agent_form.errors)
        
        response = render(request, 'rent_live/lettingagentregister.html', context={'agent_form': agent_form, 'user_form': user_form, 'registered': registered})
        return response


class LogInView(View):
    def get(self, request):
        response = render(request, 'rent_live/login.html')
        return response

    def post(self, request):
        user = request.POST.get('username')
        passw = request.POST.get('password')

        user = authenticate(username=user, password=passw)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('rent_live:index'))
            else:
                return HttpResponse("Your account has been disabled")
        else:
            print("Login Details not recognized for: {username}, {password}")
            return HttpResponse("Error: Please reenter your details and ensure that these are correct.")

class LogOutView(View):
    @method_decorator(login_required)
    def get(self, request):
        logout(request)
        response = redirect(reverse('rent_live:index'))
        return response

class UserPageView(View):
    def get_user_details(self, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None
        
        user_profile = UserProfile.objects.get_or_create(user=user)[0]
        form = UserProfileForm({'accessibleUser': user_profile.accessibleUser,'profilePic': user_profile.profilePic})

        return (user, user_profile, form)
    
    @method_decorator(login_required)
    def get(self, request, username):
        try:
            (user, user_profile, form) = self.get_user_details(username)
        except TypeError:
            return redirect(reverse('rent_live:index'))

        user_email = user.email
        try:
            is_agent = LettingAgent.objects.get(email=user_email)
        except LettingAgent.DoesNotExist:
            is_agent = None
        
        try:
            properties = Rental_Property.objects.filter(followingUsers = user)
        except Rental_Property.DoesNotExist:
            properties = None

        try:
            messages = UserMessage.objects.filter(recepient=user)
        except UserMessage.DoesNotExist:
            messages = None
        
        context_dict = {'user_profile': user_profile,'selected_user': user,'form': form, 'is_agent': is_agent, 'properties': properties, 'messages': messages}
        return render(request, 'rent_live/profile.html', context_dict)

    @method_decorator(login_required)
    def post(self, request, username):
        try:
            (user, user_profile, form) = self.get_user_details(username)
        except TypeError:
            return redirect(reverse('rent_live:index'))
        
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)

        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse('rent_live:profile',kwargs={'username': username}))
        else:
            print(form.errors)
        
        context_dict = {'user_profile': user_profile,'selected_user': user,'form': form}
        
        return render(request, 'rent_live/profile.html', context_dict)

class UserMessagesView(View):
    def get(self, request):
        return HttpResponse("This page will show the messages for the user")

class UserCommentsView(View):
    def get(self, request):
        return HttpResponse("This page will show the comments for a user")
    
class UserRentalsView(View):
    def get(self, request):
        return HttpResponse("This page will show the previously rented properties for a user.")

class AddRentalView(View):
    def get(self, request):
        added = False
        rental_form = RentalPropertyForm()

        response = render(request, 'rent_live/addroom.html', context={'rental_form': rental_form, 'added': added})
        return response

    def post(self, request):
        added = False
        rental_form = RentalPropertyForm(request.POST)

        if rental_form.is_valid():
            rental = rental_form.save(commit=False)

            if 'picture' in request.FILES:
                rental.picture = request.FILES['picture']

            rental.save()
            added = True
        else:
            print(rental_form.errors)
    
        response = render(request, 'rent_live/addroom.html', context={'rental_form': rental_form, 'added': added})
        return response

class EditProfileView(View):
    def get(self, request, username):
        form = ProfileEditForm(instance=request.user)

        response = render(request, 'rent_live/editaccount.html', context={'form': form})
        return response

    #https://www.youtube.com/watch?v=JmaxoPBvp1M&list=PLw02n0FEB3E3VSHjyYMcFadtQORvl1Ssj&index=18&ab_channel=MaxGoodridge
    def post(self, request, username):
        form = ProfileEditForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('rent_live:index'))

#https://www.youtube.com/watch?v=QxGKTvx-Vvg&list=PLw02n0FEB3E3VSHjyYMcFadtQORvl1Ssj&index=20&ab_channel=MaxGoodridge
class ChangePasswordView(View):
    def get(self, request):
        form = PasswordChangeForm(user=request.user)
        return render(request, 'rent_live/changepassword.html', context={'form': form})

        
    def post(self, request):
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user) #Stops user from being logged out.
            return redirect(reverse('rent_live:index'))
        else:
            return redirect(reverse('rent_live:index'))

#https://stackoverflow.com/questions/33715879/how-to-delete-user-in-django
class DeleteUserView(DeleteView):
    def get(self, request, username):
        return render(request, 'rent_live/delete.html', context={})
    
    def post(self, request, username):
        user = User.objects.get(username=username)
        user.delete()
        return redirect(reverse('rent_live:index'))

class LandLordView(View):
    def get(self, request):
        context_dict = {}
        landlord = Category.objects.get(name='landlord')
        agents = LettingAgent.objects.filter(category=landlord)
        context_dict['agents'] = agents
        return render(request, 'rent_live/landlords.html', context=context_dict)

class AgencyView(View):
    def get(self, request):
        context_dict = {}
        agency = Category.objects.get(name='agency')
        agents = LettingAgent.objects.filter(category=agency)
        context_dict['agents'] = agents
        return render(request, 'rent_live/agencies.html', context=context_dict)

class AgentView(View):
    def get(self, request):
        context_dict = {}
        agent = Category.objects.get(name='agent')
        agents = LettingAgent.objects.filter(category=agent)
        context_dict['agents'] = agents
        return render(request, 'rent_live/agents.html', context=context_dict)

#TWD pg 300
class FollowPropertyView(View):
    def get(self, request):
        property_name = request.GET['name']
        user = request.user

        try:
            property = Rental_Property.objects.get(name=property_name)
        except Rental_Property.DoesNotExist:
            return HttpResponse(-1)
        except ValueError:
            return HttpResponse(-1)

        property.followers = property.followers + 1
        property.followingUsers.add(user)
        property.save()

        return HttpResponse(property.followers)

class LikeCommentView(View):
    def get(self, request):
        commentID = request.GET['commentID']
        user = request.user
        profile = UserProfile.objects.get(user=user)
        profile.totalComments = profile.totalComments +1

        try:
            comment = PropertyComment.objects.get(uniqueID=commentID)
        except PropertyComment.DoesNotExist:
            return HttpResponse(-1)

        comment.likes = comment.likes + 1
        comment.likingUsers.add(user)
        comment.save()

        author = comment.user
        authorProfile = UserProfile.objects.get(user=author)
        authorProfile.totallikes = authorProfile.totallikes + 1
        authorProfile.save()

        return HttpResponse(comment.likes)

class LikeAgentComment(View):
    def get(self, request):
        commentID = request.GET['commentID']
        user = request.user
        profile = UserProfile.objects.get(user=user)
        profile.totalComments = profile.totalComments +1

        try:
            comment = AgentComment.objects.get(uniqueId=commentID)
        except AgentComment.DoesNotExist:
            return HttpResponse(-1)

        comment.likes = comment.likes + 1
        comment.likingUsers.add(user)
        comment.save()

        author = comment.user
        authorProfile = UserProfile.objects.get(user=author)
        authorProfile.totallikes = authorProfile.totallikes + 1
        authorProfile.save()

        return HttpResponse(comment.likes)

#TWD pg 308
class CitySuggestionView(View):
    def get(self, request):
        if 'suggestion' in request.GET:
            suggestion = request.GET['suggestion']
        else:
            suggestion = ''
        
        list_of_cities = get_list_of_cities(max_results=10, starts_with=suggestion)

        if len(list_of_cities) == 0:
            list_of_cities = City.objects.order_by('name')
        
        return render(request, 'rent_live/cities.html', {'cities': list_of_cities})

class ProfileFollowsView(View):
    def get(self, request):
        user = request.user
        try:
            properties = Rental_Property.objects.filter(followingUsers = user)
        except Rental_Property.DoesNotExist:
            properties = None

        context_dict = {'properties': properties}
        return render(request, 'rent_live/followedproperties.html', context=context_dict)

# Inspired by register, TWD
class SendMessageView(View):
    def get(self, request):
        message_form = UserMessageForm()
        context_dict = {}
        context_dict['message_form'] = message_form
        context_dict['recepient'] = None

        response = render(request, 'rent_live/sendmessage.html', context=context_dict)
        return response

    def post(self, request):
        message_form = UserMessageForm(request.POST)
        user = request.user
        recepient = None
        sent = False
        context_dict = {}

        if message_form.is_valid():
            message = message_form.save(commit=False)
            message.author = user
            recepient = message.recepient
            message.save()
            sent = True
        else:
            print(message_form.errors)

        context_dict['message_form'] = message_form
        context_dict['sent'] = sent
        context_dict['user'] = user
        context_dict['recepient'] = recepient

        response = render(request, 'rent_live/sendmessage.html', context=context_dict)
        return response

class LeaveCommentView(View):
    def get(self, request):
        comment_form = RentalPropertyComment()
        context_dict = {}
        context_dict['comment_form'] = comment_form

        response = render(request, 'rent_live/propertycomment.html', context=context_dict)
        return response
    
    def post(self, request):
        comment_form = RentalPropertyComment(request.POST)
        user = request.user
        context_dict = {}
        posted=False

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = user
            comment.save()
            posted=True

            property = comment.property
            property.totalCleanliness = property.totalCleanliness + comment.cleanlinessRating
            property.totalAccuracy = property.totalAccuracy + comment.accuracyRating
            property.totalEnjoyability = property.totalEnjoyability + comment.enjoyabilityRating

            property.totalRatings = property.totalRatings + 1

            property.cleanlinessRating = property.totalCleanliness/property.totalRatings
            property.accuracyRating = property.totalAccuracy/property.totalRatings
            property.enjoyabilityRating = property.totalEnjoyability/property.totalRatings

            property.save()
        else:
            print(comment_form.errors)

        context_dict['comment_form'] = comment_form

        #response = render(request, 'rent_live/propertycomment.html', context=context_dict)
        return HttpResponse("Your comment has been posted")

class AgentCommentView(View):
    def get(self, request):
        comment_form = LettingAgentComment()
        context_dict = {}
        context_dict['comment_form'] = comment_form

        response = render(request, 'rent_live/agentcomment.html', context=context_dict)
        return response

    def post(self, request):
        comment_form = LettingAgentComment(request.POST)
        user = request.user
        context_dict={}
        posted = False

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = user
            comment.save()
            posted = True

            agent = comment.agent
            agent.totalHelpfulness = agent.totalHelpfulness + comment.helpfulnessRating
            agent.totalPromptness = agent.totalPromptness + comment.promptnessRating
            agent.totalQuality = agent.totalQuality + comment.qualityRating

            agent.totalRatings = agent.totalRatings + 1

            agent.helpfulnessRating = agent.totalHelpfulness / agent.totalRatings
            agent.promptnessRating = agent.totalPromptness / agent.totalRatings
            agent.qualityRating = agent.totalQuality / agent.totalRatings

            agent.save()
        else:
            print(comment_form.errors)
        
        context_dict['comment_form'] = comment_form
        return HttpResponse("Your agent comment has been posted")
            

class MessageSentView(View):
    def get(self, request):
        return HttpResponse("Message Successfully Sent")
    
    def post(self, request):
        message_form = UserMessageForm(request.POST)
        user = request.user
        recepient = None
        sent = False
        context_dict = {}

        if message_form.is_valid():
            message = message_form.save(commit=False)
            message.author = user
            recepient = message.recepient
            message.save()
            sent = True
        else:
            print(message_form.errors)

        context_dict['message_form'] = message_form
        context_dict['sent'] = sent
        context_dict['user'] = user
        context_dict['recepient'] = recepient

        return HttpResponse("Message Successfully Sent")
    

class ShowMessagesView(View):
    def get(self, request):
        user = request.user
        
        try:
            messages = UserMessage.objects.filter(recepient=user)
        except UserMessage.DoesNotExist:
            messages = None

        context_dict = {}
        context_dict['messages'] = messages
        context_dict['user'] = user

        response = render(request, 'rent_live/showmessages.html', context=context_dict)
        return response

class ShowUserCommentsView(View):
    def get(self, request):
        user = request.user

        try:
            propertyComments = PropertyComment.objects.filter(user=user)
        except PropertyComment.DoesNotExist:
            propertyComments = None
        
        context_dict = {}
        context_dict['propertyComments'] = propertyComments

        response = render(request, 'rent_live/usercomments.html', context=context_dict)
        return response




###### HELPER FUNCTIONS ########

#TWD pg 307

def get_list_of_cities(max_results = 0, starts_with=''):
    list_of_cities = []

    if starts_with:
        list_of_cities = City.objects.filter(name__istartswith=starts_with)
    
    if max_results >0:
        if(len(list_of_cities) > max_results):
            list_of_cities = list_of_cities[:max_results]

    return list_of_cities

def get_list_of_properties(max_results=0, starts_with=' '):
    return None


