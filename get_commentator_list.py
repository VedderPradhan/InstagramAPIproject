from get_comments_list import getCommentIdList
from get_comment_info import getCommentatorAndComment

import openpyxl

commentIDs = getCommentIdList()

wb = openpyxl.Workbook()
ws1 = wb.active

for commentID in commentIDs:
    commentatorAndComment = getCommentatorAndComment(commentID)
    ws1.append(commentatorAndComment)

wb.save('CommentatorAndCommentExtract.xlsx')

    



