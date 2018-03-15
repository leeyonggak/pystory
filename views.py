from django.shortcuts import render


def index(request):
	#question_id=str(question_id)
	#by=question_id
	return render(request, 'blog/post_list.html',{})

def develop(request):
	#question_id=str(question_id)
	#by=question_id
	return render(request, 'blog/develop/develop.html',{})	

def question(request):
	#question_id=str(question_id)
	#by=question_id
	return render(request, 'blog/question/question.html',{})		