from datetime import datetime as dt
from enum import Enum


class TimestampFormat(Enum):
	"""https://discord.com/developers/docs/reference#message-formatting-timestamp-styles
	SHORT_TIME:	t: 	16:20
	LONG_TIME:	T:	16:20:30
	SHORT_DATE:	d:	20/04/2021
	LONG_DATE:	D:	20 April 2021
	SHORT_DATE_TIME:	f:	20 April 2021 16:20 (The default)
	LONG_DATE_TIME:		F:	Tuesday, 20 April 2021 16:20
	RELATIVE:	R:	2 months ago
	"""
	SHORT_TIME = 't'
	LONG_TIME = 'T'
	SHORT_DATE = 'd'
	LONG_DATE = 'D'
	SHORT_DATE_TIME = 'f'
	LONG_DATE_TIME = 'F'
	RELATIVE = 'R'


def get_timestamp(time:dt, _format=TimestampFormat.SHORT_DATE_TIME) -> str:
	"""
	Creates the string object to better represent time across timezones in Discord.

	:param datetime.datetime time: The object representing the desired time.
	:param TimestampFormat _format: The value from the TimestampFormat enum representing how you want the time to look.
	:return: The string to use.
	"""
	if not isinstance(_format, TimestampFormat):
		raise ValueError(f"The given format must be from the TimestampFormat enum class or a string with the raw format. Not {type(format).__name__}")
	timestamp = int(time.timestamp())
	return f"<t:{timestamp}:{_format.value}>"


def full_author_name(author) -> str:
	from interactions import Member

	if isinstance(author, Member):
		return f"{author.user.username}#{author.user.discriminator}"

	return f"{author.name}#{author.discriminator}"

