#Abdirahman Mohamed CSC 335 Project 6
import re

NUM     = 1     # number e.g. '123'
ID      = 2     # symbol e.g. 'LOOP'
OP      = 3     # = ; ( ) @ + - & | !
ERROR   = 4     # error in file

class Lex(object):
    def __init__(self, file_name):
        """Assumes input will be program-generated. Detects numbers, Ids, and operators.
Reads the whole .asm program into memory and uses regular expressions to match lexical tokens."""
        file = open(file_name, 'r')
        self._lines = file.read()
        self._tokens = self._tokenize(self._lines.split('\n'))
        self.cur_command = []        # list of tokens for current command
        self.cur_token = (ERROR,0)   # current token of current command

    def __str__(self):
        pass

    def has_more_commands(self):
        """Returns a list of tokens for current command"""
        return self._tokens != []

    def next_command(self):
        """Gets the next command"""
        self.cur_command = self._tokens.pop(0) # the current command would be the first token
        self.next_token() # gets the next token
        return self.cur_command

    def has_next_token(self):
        """Returns a list of commands that have tokens"""
        return self.cur_command != []

    def next_token(self):
        """Gets the next token"""
        if self.has_next_token(): # if there are tokens in commands
            self.cur_token = self.cur_command.pop(0) # the current token would be the first commmand
        else: # if there aren't any commands
            self.cur_token = (ERROR, 0) # returns error
        return self.cur_token

    def peek_token(self):
        """Returns the first token in the commands """
        if self.has_next_token(): # if there are tokens in commands
            return self.cur_command[0] # reuturns the top element in the command
        else: # if there aren't any tokens in commands
            return (ERROR, 0) # returns an error

    def _tokenize(self, lines):
        """Returns the lines in commands"""
        return [t for t in [self._tokenize_line(l) for l in lines] if t!=[]]

    def _tokenize_line(self, line):
        """Returns the words in lines including comments"""
        return [self._token(word) for word in self._split(self._remove_comment(line))]

    _comment = re.compile('//.*$') # get comments
    def _remove_comment(self, line):
        """Removes the comments and returns the lines without the comments"""
        return self._comment.sub('', line)

    _num_re = r'\d+' # the number
    _id_start = r'\w_.$:' # the start of an id
    _id_re = '['+_id_start+']['+_id_start+r'\d]*' # the complete id
    _op_re = r'[=;()@+\-&|!]' # the operation
    _word = re.compile(_num_re+'|'+_id_re+'|'+_op_re) # the words in lines
    def _split(self, line):
        """Returns the splitted words in lines"""
        return self._word.findall(line)

    def _token(self, word):
        """Identifies the words in lines and distinguish them"""
        if   self._is_num(word):     return (NUM, word) # if it is a number it will return a number
        elif self._is_id(word):      return (ID, word)  # if it is an id it will return an id
        elif self._is_op(word):      return (OP, word)  # if it is an operation it will return an operation
        else:                        return (ERROR, word)

    def _is_op(self, word):
        """Returns the operation"""
        return self._is_match(self._op_re, word)

    def _is_num(self, word):
        """Returns the number"""
        return self._is_match(self._num_re, word)

    def _is_id(self, word):
        """Returns the id"""
        return self._is_match(self._id_re, word)

    def _is_match(self, re_str, word):
        """Matches the words with their corresponding definitions"""
        return re.match(re_str, word) != None
