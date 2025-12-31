from rolepermissions.roles import AbstractUserRole


class Professor(AbstractUserRole):
    available_permissions = {
        'view_all_content':True,
        'upload_content':True,
        'approve_content':True,
        'moderate_forum':True,
        'view_student_progress':True,
        'edit_own_profile':True
    }



class Aluno(AbstractUserRole):
    available_permissions = {
        'view_content':True,
        'upload_content':True,
        'take_quizzes':True,
        'post_question':True,
        'reply_question':True,
        'view_leaderboard':True,
        'edit_own_profile':True,
    }