#!/usr/bin/env python3

class MyString:
    def __init__(self, first_value=''):
        self.value = first_value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print('The value must be a string.')
    
    def is_sentence(self):
        return self.value[-1] == '.'
    
    def is_question(self):
        return self.value[-1] == '?'
    
    def is_exclamation(self):
        return self.value[-1] == '!'
    
    # solution A
    def count_sentences(self):
        new_value = self.value.replace('!', '.').replace('?', '.')
        l = new_value.split('.')
        count = 0
        for item in l:
            if len(item) != 0:
                count += 1
        return count
    
    # solution B
    # def count_sentences(self):
    #     new_value = self.value.replace('!', '.').replace('?', '.')
    #     l = new_value.split('. ')
    #     return len(l)


s1 = MyString('This, well, is a sentence. This is too!! And so is this, I think? Woo...')
print(s1.count_sentences())