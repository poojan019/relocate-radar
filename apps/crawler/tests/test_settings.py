from scrapy.settings import Settings

from relocate_crawler import settings as crawler_settings


def _load() -> Settings:
    s = Settings()
    s.setmodule(crawler_settings, priority="project")
    return s


def test_obeys_robots_txt() -> None:
    assert _load().getbool("ROBOTSTXT_OBEY") is True


def test_autothrottle_enabled() -> None:
    assert _load().getbool("AUTOTHROTTLE_ENABLED") is True


def test_user_agent_identifies_the_bot() -> None:
    user_agent = _load().get("USER_AGENT")
    assert "RelocateRadarBot" in user_agent
    assert "github.com/poojan019/relocate-radar" in user_agent
