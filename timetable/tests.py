from datetime import time

import pytest

from timetable.models import Session


@pytest.mark.django_db
def test_session_str_has_name_and_day():
    s = Session.objects.create(
        day=1, start_time=time(19, 0), end_time=time(20, 0), name="Intervals"
    )
    text = str(s)
    assert "Intervals" in text and "Mon" in text
