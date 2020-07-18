from get_comments_list import getCommentIdList
from get_comment_info import getCommentatorAndComment

from openpyxl.styles import PatternFill
import openpyxl
import re

commentIDs = getCommentIdList()

fileName = 'CommentatorAndCommentList.xlsx'
wb = openpyxl.Workbook()
ws1 = wb.active

count = 1
for commentID in commentIDs:
    commentatorAndComment = getCommentatorAndComment(commentID)
    ws1.append(commentatorAndComment)
    print("Inserting in Excel..." + str(count) + "/" + str(len(commentIDs)))
    count = count + 1
wb.save(fileName)


    

    



