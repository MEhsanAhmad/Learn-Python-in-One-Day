sessions = 4
for session in range(1, sessions + 1):
    print(f"\n Starting Study Session {session} of {sessions}...")
    print("Study for 25 minutes.")
    if session < sessions:
        print("✅ Session complete! Take a 5-minute break.")
    else:
        print("🎉 All sessions complete! Take a long 30-minute break.")
