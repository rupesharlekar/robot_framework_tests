*** Settings ***
Library     Modules.api.bhagwadgita_api.ChapterVerse

*** Keywords ***

API is authenticated for CLIENT_ID and CLIENT_SECRET
    authenticate_client

Verify there are total "${chapter_count}" chapters in bhagwad gita
    verify_chapters_count  ${chapter_count}

Verify chapter "${chapter_no}" name meaning is "${name_meaning}"
    verify_chapter_meaning  chapter_no=${chapter_no}  exp_name_meaning=${name_meaning}

Verify in chapter "${chapter_no}" there are total "${verse_count}" verses in bhagwad gita
    verify_verse_count_in_chapter  chapter_no=${chapter_no}  verse_count=${verse_count}

Verify verse "${verse_number}" of chapter "${chapter_no}" starts with "${meaning}"
    verify_meaning_of_verse_number  verse_number=${verse_number}  chapter_no=${chapter_no}  meaning=${meaning}