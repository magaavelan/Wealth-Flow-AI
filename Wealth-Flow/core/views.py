from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import ChatSession, ChatMessage
from .agent import query_ai_workflow

def dashboard_home(request):
    """Renders the main layout panel showing historical chat sessions and active workspaces."""
    # Retrieve all distinct conversation sessions to populate the sidebar list
    sessions = ChatSession.objects.all().order_by('-created_at')
    
    context = {
        'sessions': sessions,
        'active_session': None,
        'messages': []
    }
    return render(request, 'core/dashboard.html', context)


def chat_session_detail(request, session_id):
    """Loads a specific historical chat log and opens the conversation panel workspace."""
    sessions = ChatSession.objects.all().order_by('-created_at')
    active_session = get_object_or_404(ChatSession, id=session_id)
    
    # Retrieve all existing messages belonging to this current open thread
    messages = active_session.messages.all().order_by('timestamp')
    
    context = {
        'sessions': sessions,
        'active_session': active_session,
        'messages': messages
    }
    return render(request, 'core/dashboard.html', context)


def create_new_session(request):
    """Instantly spins up an isolated, empty conversational thread channel."""
    new_session = ChatSession.objects.create(title="New Antigravity Chat")
    return redirect('chat_session_detail', session_id=new_session.id)


def send_message_api(request, session_id):
    """
    API endpoint handling incoming asynchronous AJAX POST payloads from our UI form.
    Executes the Antigravity multi-turn reasoning workflow loop.
    """
    if request.method == "POST":
        session = get_object_or_404(ChatSession, id=session_id)
        user_text = request.POST.get("message", "").strip()
        
        if not user_text:
            return JsonResponse({"error": "Empty prompt content message rejected."}, status=400)
            
        # 1. Save the incoming human user message to the Django SQLite Database
        ChatMessage.objects.create(session=session, role='user', content=user_text)
        
        # 2. Extract historical messages in this thread context to guide the agent
        raw_history = session.messages.all().order_by('timestamp')
        history_list = [{"role": msg.role, "content": msg.content} for msg in raw_history]
        
        try:
            # 3. Dispatches payload execution directly to our Google Antigravity Agent runtime block
            ai_response_text = query_ai_workflow(user_text, history_list)
            
            # 4. Save the final processed response output string to our historical database
            ChatMessage.objects.create(session=session, role='assistant', content=ai_response_text)
            
            # If this was the very first interaction, dynamically rename the chat title automatically
            if session.title == "New Antigravity Chat" and len(user_text) < 40:
                session.title = user_text
                session.save()
                
            return JsonResponse({
                "status": "success",
                "user_message": user_text,
                "ai_response": ai_response_text,
                "session_title": session.title
            })
            
        except Exception as e:
            return JsonResponse({"error": f"Antigravity Runtime execution fault: {str(e)}"}, status=500)
            
    return JsonResponse({"error": "Invalid request protocol method."}, status=405)