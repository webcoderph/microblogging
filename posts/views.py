from django.shortcuts import render_to_response
from posts.models import Post
from forms import PostForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required



@login_required
def posts(request):
	posts_list = Post.objects.all()
	paginator = Paginator(posts_list, 3)

	page = request.GET.get('page')

	try:
		post_page = paginator.page(page)
	except PageNotAnInteger:
		post_page = paginator.page(1)
	except EmptyPage:
		post_page = paginator.page(paginator.num_pages)		

    	return render_to_response('posts.html',
							 {'posts': post_page,'full_name': request.user.username})


def post(request, post_id = 1):
	return render_to_response('post.html',
							 {'post': Post.objects.get(id=post_id)})

@login_required
def create(request):
	if request.POST:
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/posts/all/')

	else:
	    form = PostForm()


	args = {}
	args.update(csrf(request))  
	args['uid'] = request.user.id
	args['form'] = form

	return render_to_response('create.html', args)  				