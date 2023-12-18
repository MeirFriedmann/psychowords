from bardapi import Bard

token = 'z-pz9vRlBujzCRjp/AMr4Oo5Ze-c8wL_MS'
bard = Bard(token=token)
bard.get_answer("how are you?")['content']
