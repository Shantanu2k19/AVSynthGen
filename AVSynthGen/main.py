import GPTApis

#GPTApis.CheckGPTConnection()

def main():
    print("Asking to ChatGPT")
    prompt = "tell me recipe of dhokla"
    GPTApis.GetGPTResponse(prompt)

if __name__ == "__main__":
    main()
