from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from rent_live.models import Category, LettingAgent, City, Rental_Property, User, Comment, UserProfile
from rent_live.forms import UserForm, UserProfileForm, AgentProfileForm, RentalPropertyForm, ProfileEditForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.views.generic.edit import DeleteView


# Create your views here.
class myss(View):
    def get(self, request):
        response = render(request, 'rent_live/html.html')

        return response




class IndexView(View):
    def get(self, request):
        property_list = Rental_Property.objects.order_by('-followers')[:3]
        lettingagent_list = LettingAgent.objects.order_by('-qualityRating')[:3]
        city_list = City.objects.order_by('name')

        context_dict = {}
        context_dict['properties'] = property_list
        context_dict['lettingAgents'] = lettingagent_list
        context_dict['city'] = city_list

        response = render(request, 'rent_live/index.html', context=context_dict)

        return response

class AboutView(View):
    def get(self, request):
        response = render(request, 'rent_live/about.html', context={})
        return response

class ContactView(View):
    def get(self, request):
        response = render(request, 'rent_live/contact.html', context={})
        return response

class SearchView(View):
    def get(self, request):
        response = render(request, 'rent_live/search.html', context={})
        return response

class SearchResultView(View):
    def get(self, request):
        return HttpResponse("This is the search result page, which will show the search results for each search.")

class CityView(View):
    def get_city_details(self, cityname):
        context_dict = {}

        try:
            city = City.objects.get(slug=cityname)
            rental_properties = Rental_Property.objects.filter(city=cityname)
            agents = LettingAgent.objects.filter(city=cityname)

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

        response = render(request, 'rent_live/rentalproperty.html', context=context_dict)
        return response

class PropertyView(View):
    def get(self, request):
        return HttpResponse("This is the page for a specific property")

class LettingAgentsView(View):
    def get(self, request):
        return HttpResponse("This is the page detailing different letting agents")

class LettingAgentView(View):
    def get_agent(self, letting_agent_name_slug):
        context_dict = {}

        try:
            letting_agent = LettingAgent.objects.get(slug=letting_agent_name_slug)
            agent_properties = Rental_Property.objects.filter(lettingAgent = letting_agent)
            context_dict['agent'] = letting_agent
            context_dict['properties'] = agent_properties
        except LettingAgent.DoesNotExist:
            context_dict['agent'] = None
            context_dict['properties'] = None
        
        return context_dict
   
    def get(self, request, letting_agent_name_slug):
        context_dict = self.get_agent(letting_agent_name_slug)
        
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

            if 'profilePic' in request.FILES:
                profile.profilePic = request.FILES['profilePic']
                print("test")

            profile.save()
            registered = True
            print("test2")
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
                agent.logo = request.FILE['logo']
            
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

    def get(self, request, username):
        try:
            (user, user_profile, form) = self.get_user_details(username)
        except TypeError:
            return redirect(reverse('rent_live:index'))

        is_agent = LettingAgent.objects.filter(email=user.email)
        
        context_dict = {'user_profile': user_profile,'selected_user': user,'form': form, 'is_agent': is_agent}
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
        model = User
        success_url = reverse('rent_live:index')

        return render(request, 'rent_live/delete.html', context={})
    
    def post(self, request, username):
        user = User.objects.get(username=username)
        user.delete()
        return redirect(reverse('rent_live:index'))
