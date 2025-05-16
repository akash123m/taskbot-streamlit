from nlp_parser import extract_intent
import storage

def respond(user_input):
    try:
        parsed = extract_intent(user_input)
        intent = parsed.get("intent")

        if intent == "add_task":
            task = parsed.get("task")
            time = parsed.get("time")
            storage.add_task(task, time)
            return f"✅ Task added: '{task}' at {time}"
        
        elif intent == "show_tasks":
            tasks = storage.get_tasks()
            if not tasks:
                return "📭 No tasks yet."
            return "\n".join([f"{i+1}. {t['task']} - {t['status']} at {t['time']}" for i, t in enumerate(tasks)])
        
        elif intent == "mark_done":
            index = parsed.get("index", 1) - 1
            storage.mark_done(index)
            return f"✅ Marked task #{index+1} as done."

        elif intent == "delete_task":
            index = parsed.get("index", 1) - 1
            storage.delete_task(index)
            return f"🗑️ Deleted task #{index+1}."
        
        return "🤔 Sorry, I didn’t understand that."
    except Exception as e:
        return f"⚠️ Error: {str(e)}"
