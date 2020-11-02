import os

def make_directories(section, folders):
    if not os.path.exists(os.path.join('.', section)):
        os.mkdir(section)
    for line in folders:
        path = os.path.join('.', section, line)
        if not os.path.exists(path):
            os.mkdir(path)

subject_directories = [
    '.admin',
    '.resources',
    '001_unit_outlines',
    '002_assessment_items',
    '003_learning_briefs',
    '004_flipped_videos'
]

make_directories("subject_directories", subject_directories)


admin_directories = [
    '.admin',
    '.documents',
    '.moderation',
    '.purchases',
    '.reporting',
    '.resources'
]


make_directories("admin_directories", admin_directories)

moderation_directorgies = [
    'SubjectA',
    'SubjectB'
]

make_directories("moderation_directorgies", moderation_directorgies)

moderation_subject_directories = [
    '001_condition_report',
    '002_presentation_review_proformer_PRP',
    '003_unit_outline',
    '004_conditions_relevant_to_assessment',
    '005_clean_assessment_tasks',
    '006_student_portfolio_a',
    '007_student_portfolio_b',
    '008_other_evidence'
]

make_directories("moderation_subject_directories", moderation_subject_directories)

student_portfolio_directories = [
    '001_assessment_item_1',
    '002_assessment_item_2',
    '003_assessment_item_3',
    '004_assessmment_item_4'
]

make_directories("student_portfolio_directories", student_portfolio_directories)


