'''
Created on Jun 04, 2018
@author: Felix Ding

Word Ladder II

Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:
    Only one letter can be changed at a time
    Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

Note:
    Return an empty list if there is no such transformation sequence.
    All words have the same length.
    All words contain only lowercase alphabetic characters.
    You may assume no duplicates in the word list.
    You may assume beginWord and endWord are non-empty and are not the same.
'''

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        ladder = [['a','b'],['c','d']]

        
        return ladder
        

if __name__ == '__main__':
        beginWord="hit"
        endWord="cog"
        wordList=["hot","dot","dog","lot","log","cog"]
        ladder = Solution().findLadders(beginWord, endWord, wordList)
        print(ladder)
