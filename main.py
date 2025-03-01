import socket

def connect_to_service():
    host = "benchmark.challs.cyberchallenge.it"
    port = 9031
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    return s

def send_password(s, password):
    # Send the password to the service
    s.sendall(password.encode() + b"\n")
    
    # Receive the response (including clock cycles)
    response = s.recv(1024).decode()
    return response

def extract_cycles(response):
    # Look for the part that gives us the clock cycles in the response
    # Example: "Wrong password, checked in 161 clock cycles"
    if "clock cycles" in response:
        start = response.find("checked in") + len("checked in ")
        end = response.find(" clock cycles")
        cycles = int(response[start:end])
        return cycles
    return None

def test_passwords():
    # List of password guesses to try
    guesses = [
        "password123",
        "something",
        "boh",
        "admin",
        "12345",
        "qwerty",
        "password1234",
        "password123!"
    ]
    
    # Connect to the service
    s = connect_to_service()
    
    for guess in guesses:
        print(f"Trying password: {guess}")
        response = send_password(s, guess)
        cycles = extract_cycles(response)
        
        if cycles is not None:
            print(f"Password '{guess}' checked in {cycles} clock cycles")
        else:
            print(f"No clock cycles found for password '{guess}'")
    
    # Close the connection
    s.close()

if __name__ == "__main__":
    test_passwords()
