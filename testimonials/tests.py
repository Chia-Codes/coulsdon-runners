import pytest

from testimonials.models import Testimonial


@pytest.mark.django_db
def test_testimonial_str():
    t = Testimonial.objects.create(
        author="Alex", quote="Great sessions!", is_featured=True
    )
    assert "Alex" in str(t)
