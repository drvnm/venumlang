INTEGER, PLUS, MIN, EOF = "INTEGER", "PLUS", "MIN", "EOF" # Token types


# THIS IS A WORK IN PROGRESS


class Token:
    def __init__(self, type, value):
        # Token type e.g ointeger. plus (operator) or eof
        self.type = type
        # token value: real number, + (operator) or None
        self.value = value
    
    def __str__(self):
        # string representation of a taken, e.g. Token(INTEGER, 3)
        return f"Token({self.type}, {self.value})"
    
    def __repr__(self):
        return self.__str__()
    
class Interpreter:
    def __init__(self, text):
        # input of program, e.g 3 + 2
        self.text = text
        # position of program
        self.pos = 0
        # start token
        self.current_token = None
        self.current_char = text[self.pos]
    
    def error(self):
        raise Exception("Error parsing input")
        
    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]
    
    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()
    
    def integer(self):
        result = ""
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)
    
    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            
            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())
            
            if self.current_char == '+':
                self.advance()
                return Token(PLUS, '+')
            
            if self.current_char == '-':
                self.advance()
                return Token(MIN, '-')
            
            self.error()
        return Token(EOF, None)
    
    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()
    
    def term(self):
        token = self.current_token
        self.eat(INTEGER)
        return token.value
            
    def expr(self):
        self.current_token = self.get_next_token()
        
        result = self.term()
        while self.current_token.type in (PLUS, MIN):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
                result = result + self.term()
            elif token.type == MIN:
                self.eat(MIN)
                result = result - self.term()

        return result
                
    

def main():
    while True:
        try:
            text = input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)
        
if __name__ == '__main__':
    main()