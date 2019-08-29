# -*- coding: utf-8 -*-

from transporthours.main import Main
import unittest

class MainTest(unittest.TestCase):
	#
	# tagsToGtfs
	#
	def test_tagsToGtfs_works_singlerange(self):
		tags = {
			"type": "route",
			"route": "bus",
			"name": "Ligne 42",
			"opening_hours": "Mo-Fr 05:00-22:00",
			"interval": "00:30",
			"interval:conditional": "00:10 @ (Mo-Fr 07:00-09:30, 16:30-19:00)"
		}
		result = Main().tagsToGtfs(tags)
		expected = [
			{ "monday": True, "tuesday": True, "wednesday": True, "thursday": True, "friday": True, "saturday": False, "sunday": False, "start_time": "05:00:00", "end_time": "07:00:00", "headway": 1800 },
			{ "monday": True, "tuesday": True, "wednesday": True, "thursday": True, "friday": True, "saturday": False, "sunday": False, "start_time": "07:00:00", "end_time": "09:30:00", "headway": 600 },
			{ "monday": True, "tuesday": True, "wednesday": True, "thursday": True, "friday": True, "saturday": False, "sunday": False, "start_time": "09:30:00", "end_time": "16:30:00", "headway": 1800 },
			{ "monday": True, "tuesday": True, "wednesday": True, "thursday": True, "friday": True, "saturday": False, "sunday": False, "start_time": "16:30:00", "end_time": "19:00:00", "headway": 600 },
			{ "monday": True, "tuesday": True, "wednesday": True, "thursday": True, "friday": True, "saturday": False, "sunday": False, "start_time": "19:00:00", "end_time": "22:00:00", "headway": 1800 }
		]
		self.assertEqual(result, expected)

	def test_tagsToGtfs_works_multiranges(self):
		tags = {
			"type": "route",
			"route": "bus",
			"name": "Ligne 42",
			"opening_hours": "Mo-Fr 05:00-22:00; Sa 07:00-23:00",
			"interval": "00:10",
			"interval:conditional": "5 @ (Mo,Fr 08:00-10:00,16:30-18:30); 00:06 @ (Sa 11:00-13:00)"
		}
		result = Main().tagsToGtfs(tags)
		expected = [
			{ "monday": True, "tuesday": False, "wednesday": False, "thursday": False, "friday": True, "saturday": False, "sunday": False, "start_time": "05:00:00", "end_time": "08:00:00", "headway": 600 },
			{ "monday": True, "tuesday": False, "wednesday": False, "thursday": False, "friday": True, "saturday": False, "sunday": False, "start_time": "08:00:00", "end_time": "10:00:00", "headway": 300 },
			{ "monday": True, "tuesday": False, "wednesday": False, "thursday": False, "friday": True, "saturday": False, "sunday": False, "start_time": "10:00:00", "end_time": "16:30:00", "headway": 600 },
			{ "monday": True, "tuesday": False, "wednesday": False, "thursday": False, "friday": True, "saturday": False, "sunday": False, "start_time": "16:30:00", "end_time": "18:30:00", "headway": 300 },
			{ "monday": True, "tuesday": False, "wednesday": False, "thursday": False, "friday": True, "saturday": False, "sunday": False, "start_time": "18:30:00", "end_time": "22:00:00", "headway": 600 },
			{ "monday": False, "tuesday": True, "wednesday": True, "thursday": True, "friday": False, "saturday": False, "sunday": False, "start_time": "05:00:00", "end_time": "22:00:00", "headway": 600 },
			{ "monday": False, "tuesday": False, "wednesday": False, "thursday": False, "friday": False, "saturday": True, "sunday": False, "start_time": "07:00:00", "end_time": "11:00:00", "headway": 600 },
			{ "monday": False, "tuesday": False, "wednesday": False, "thursday": False, "friday": False, "saturday": True, "sunday": False, "start_time": "11:00:00", "end_time": "13:00:00", "headway": 360 },
			{ "monday": False, "tuesday": False, "wednesday": False, "thursday": False, "friday": False, "saturday": True, "sunday": False, "start_time": "13:00:00", "end_time": "23:00:00", "headway": 600 }
		]
		self.assertEqual(result, expected)

	def test_tagsToGtfs_ignore_ph(self):
		tags = {
			"type": "route",
			"route": "bus",
			"name": "Ligne 42",
			"opening_hours": "Mo-Fr,PH 05:00-22:00",
			"interval": "00:30",
			"interval:conditional": "00:10 @ (Mo-Fr 07:00-09:30, 16:30-19:00); 00:30 @ (PH 05:00-22:00)"
		}
		result = Main().tagsToGtfs(tags)
		expected = [
			{ "monday": True, "tuesday": True, "wednesday": True, "thursday": True, "friday": True, "saturday": False, "sunday": False, "start_time": "05:00:00", "end_time": "07:00:00", "headway": 1800 },
			{ "monday": True, "tuesday": True, "wednesday": True, "thursday": True, "friday": True, "saturday": False, "sunday": False, "start_time": "07:00:00", "end_time": "09:30:00", "headway": 600 },
			{ "monday": True, "tuesday": True, "wednesday": True, "thursday": True, "friday": True, "saturday": False, "sunday": False, "start_time": "09:30:00", "end_time": "16:30:00", "headway": 1800 },
			{ "monday": True, "tuesday": True, "wednesday": True, "thursday": True, "friday": True, "saturday": False, "sunday": False, "start_time": "16:30:00", "end_time": "19:00:00", "headway": 600 },
			{ "monday": True, "tuesday": True, "wednesday": True, "thursday": True, "friday": True, "saturday": False, "sunday": False, "start_time": "19:00:00", "end_time": "22:00:00", "headway": 1800 }
		]
		self.assertEqual(result, expected)

	def test_tagsToGtfs_empty_if_unset(self):
		tags = {
			"type": "route",
			"route": "bus",
			"name": "Ligne 42"
		}
		result = Main().tagsToGtfs(tags)
		expected = []
		self.assertEqual(result, expected)

	def test_tagsToGtfs_error_if_invalid(self):
		tags = {
			"type": "route",
			"route": "bus",
			"name": "Ligne 42",
			"opening_hours": "this is broken",
			"interval": "00:10"
		}
		self.assertRaises(Exception, Main().tagsToGtfs, tags)

	#
	# tagsToHoursObject
	#
	def test_tagsToHoursObject_handles_all_tags_set(self):
		tags = {
			"type": "route",
			"route": "bus",
			"name": "Ligne 42",
			"opening_hours": "Mo-Fr 05:00-22:00",
			"interval": "00:30",
			"interval:conditional": "00:10 @ (Mo-Fr 07:00-09:30, 16:30-19:00)"
		}
		result = Main().tagsToHoursObject(tags)
		expected = {
			"opens": {
				"mo": ["05:00-22:00"],
				"tu": ["05:00-22:00"],
				"we": ["05:00-22:00"],
				"th": ["05:00-22:00"],
				"fr": ["05:00-22:00"],
				"sa": [],
				"su": [],
				"ph": []
			},
			"defaultInterval": 30,
			"otherIntervals": [
				{
					"interval": 10,
					"applies": {
						"mo": ["07:00-09:30", "16:30-19:00"],
						"tu": ["07:00-09:30", "16:30-19:00"],
						"we": ["07:00-09:30", "16:30-19:00"],
						"th": ["07:00-09:30", "16:30-19:00"],
						"fr": ["07:00-09:30", "16:30-19:00"],
						"sa": [],
						"su": [],
						"ph": []
					}
				}
			],
			"otherIntervalsByDays": [
				{ "days": [ "mo", "tu", "we", "th", "fr" ], "intervals": { "07:00-09:30": 10, "16:30-19:00": 10 } }
			],
			"allComputedIntervals": [
				{ "days": [ "mo", "tu", "we", "th", "fr" ], "intervals": { "05:00-07:00": 30, "07:00-09:30": 10, "09:30-16:30": 30, "16:30-19:00": 10, "19:00-22:00": 30 } }
			]
		}
		self.assertEqual(result, expected)

	def test_tagsToHoursObject_handles_no_intervalconditional_tag(self):
		tags = {
			"type": "route",
			"route": "bus",
			"name": "Ligne 42",
			"opening_hours": "Mo-Fr 05:00-22:00",
			"interval": "00:30"
		}
		result = Main().tagsToHoursObject(tags)
		expected = {
			"opens": {
				"mo": ["05:00-22:00"],
				"tu": ["05:00-22:00"],
				"we": ["05:00-22:00"],
				"th": ["05:00-22:00"],
				"fr": ["05:00-22:00"],
				"sa": [],
				"su": [],
				"ph": []
			},
			"defaultInterval": 30,
			"otherIntervals": "unset",
			"otherIntervalsByDays": "unset",
			"allComputedIntervals": [
				{ "days": [ "mo", "tu", "we", "th", "fr" ], "intervals": { "05:00-22:00": 30 } }
			]
		}
		self.assertEqual(result, expected)

	def test_tagsToHoursObject_handles_no_opening_hours_tag(self):
		tags = {
			"type": "route",
			"route": "bus",
			"name": "Ligne 42",
			"interval": "00:30"
		}
		result = Main().tagsToHoursObject(tags)
		expected = {
			"opens": "unset",
			"defaultInterval": 30,
			"otherIntervals": "unset",
			"otherIntervalsByDays": "unset",
			"allComputedIntervals": [
				{ "days": [ "mo", "tu", "we", "th", "fr", "sa", "su", "ph" ], "intervals": { "00:00-24:00": 30 } }
			]
		}
		self.assertEqual(result, expected)

	def test_tagsToHoursObject_handles_no_tags(self):
		tags = {
			"type": "route",
			"route": "bus",
			"name": "Ligne 42"
		}
		result = Main().tagsToHoursObject(tags)
		expected = {
			"opens": "unset",
			"defaultInterval": "unset",
			"otherIntervals": "unset",
			"otherIntervalsByDays": "unset",
			"allComputedIntervals": "unset"
		}
		self.assertEqual(result, expected)

	def test_tagsToHoursObject_handles_opening_hours_invalid(self):
		tags = {
			"type": "route",
			"route": "bus",
			"name": "Ligne 42",
			"opening_hours": "what ?",
			"interval": "00:30"
		}
		result = Main().tagsToHoursObject(tags)
		expected = {
			"opens": "invalid",
			"defaultInterval": 30,
			"otherIntervals": "unset",
			"otherIntervalsByDays": "unset",
			"allComputedIntervals": "invalid"
		}
		self.assertEqual(result, expected)

	def test_tagsToHoursObject_handles_interval_invalid(self):
		tags = {
			"type": "route",
			"route": "bus",
			"name": "Ligne 42",
			"interval": "12 minutes is so long to wait for a bus..."
		}
		result = Main().tagsToHoursObject(tags)
		expected = {
			"opens": "unset",
			"defaultInterval": "invalid",
			"otherIntervals": "unset",
			"otherIntervalsByDays": "unset",
			"allComputedIntervals": "invalid"
		}
		self.assertEqual(result, expected)

	def test_tagsToHoursObject_handles_intervalconditional_invalid(self):
		tags = {
			"type": "route",
			"route": "bus",
			"name": "Ligne 42",
			"interval": "00:30",
			"interval:conditional": "12 @ random hours"
		}
		result = Main().tagsToHoursObject(tags)
		expected = {
			"opens": "unset",
			"defaultInterval": 30,
			"otherIntervals": "invalid",
			"otherIntervalsByDays": "invalid",
			"allComputedIntervals": "invalid"
		}
		self.assertEqual(result, expected)

	#
	# intervalConditionalStringToObject
	#
	def test_intervalConditionalStringToObject_handles_standard_tag(self):
		intervalCond = "00:05 @ (Mo-Fr 07:00-10:00); 00:10 @ (Mo-Fr 16:30-19:00); 00:30 @ (Mo-Su 22:00-05:00)"
		result = Main().intervalConditionalStringToObject(intervalCond)
		expected = [
			{
				"interval": 5,
				"applies": {
					"mo": ["07:00-10:00"],
					"tu": ["07:00-10:00"],
					"we": ["07:00-10:00"],
					"th": ["07:00-10:00"],
					"fr": ["07:00-10:00"],
					"sa": [],
					"su": [],
					"ph": []
				}
			},
			{
				"interval": 10,
				"applies": {
					"mo": ["16:30-19:00"],
					"tu": ["16:30-19:00"],
					"we": ["16:30-19:00"],
					"th": ["16:30-19:00"],
					"fr": ["16:30-19:00"],
					"sa": [],
					"su": [],
					"ph": []
				}
			},
			{
				"interval": 30,
				"applies": {
					"mo": ["22:00-05:00"],
					"tu": ["22:00-05:00"],
					"we": ["22:00-05:00"],
					"th": ["22:00-05:00"],
					"fr": ["22:00-05:00"],
					"sa": ["22:00-05:00"],
					"su": ["22:00-05:00"],
					"ph": []
				}
			},
		]
		self.assertEqual(result, expected)

	#
	# _splitMultipleIntervalConditionalString
	#

	def test_splitMultipleIntervalConditionalString_handles_string_nosemicolons_in_oh_part(self):
		intervalCond = "00:05 @ (Mo-Fr 07:00-10:00); 00:05 @ (Mo-Fr 16:30-19:00); 00:30 @ (Mo-Su 22:00-05:00)"
		result = Main()._splitMultipleIntervalConditionalString(intervalCond)
		expected = ["00:05 @ (Mo-Fr 07:00-10:00)","00:05 @ (Mo-Fr 16:30-19:00)","00:30 @ (Mo-Su 22:00-05:00)"]
		self.assertEqual(result, expected)

	def test_splitMultipleIntervalConditionalString_handles_string_withsemicolons_in_ohpart(self):
		intervalCond = "00:05 @ (Mo-Fr 07:00-10:00 ; Su 16:30-19:00) ; 00:30 @ (Mo-Su 22:00-05:00)"
		result = Main()._splitMultipleIntervalConditionalString(intervalCond)
		expected = ["00:05 @ (Mo-Fr 07:00-10:00 ; Su 16:30-19:00)","00:30 @ (Mo-Su 22:00-05:00)"]
		self.assertEqual(result, expected)

	#
	# _readSingleIntervalConditionalString
	#

	def test_readSingleIntervalConditionalString_handles_basic(self):
		intervalCond = "00:10 @ (Sa-Su 06:00-22:00)"
		result = Main()._readSingleIntervalConditionalString(intervalCond)
		expected = {
			"interval": 10,
			"applies": {
				"mo": [],
				"tu": [],
				"we": [],
				"th": [],
				"fr": [],
				"sa": ["06:00-22:00"],
				"su": ["06:00-22:00"],
				"ph": []
			}
		}
		self.assertEqual(result, expected)

	def test_readSingleIntervalConditionalString_handles_oh_without_quotes(self):
		intervalCond = "15 @ Mo 06:00-22:00"
		result = Main()._readSingleIntervalConditionalString(intervalCond)
		expected = {
			"interval": 15,
			"applies": {
				"mo": ["06:00-22:00"],
				"tu": [],
				"we": [],
				"th": [],
				"fr": [],
				"sa": [],
				"su": [],
				"ph": []
			}
		}
		self.assertEqual(result, expected)

	def test_readSingleIntervalConditionalString_handles_nospaces(self):
		intervalCond = "15@Mo 06:00-22:00"
		result = Main()._readSingleIntervalConditionalString(intervalCond)
		expected = {
			"interval": 15,
			"applies": {
				"mo": ["06:00-22:00"],
				"tu": [],
				"we": [],
				"th": [],
				"fr": [],
				"sa": [],
				"su": [],
				"ph": []
			}
		}
		self.assertEqual(result, expected)

	#
	# _intervalConditionObjectToIntervalByDays
	#

	def test_intervalConditionObjectToIntervalByDays_works_distinct_days(self):
		intvObj = [
			{ "interval": 10, "applies": { "mo": [ "00:00-01:00" ], "tu": [ "01:00-02:00" ], "we": [ "02:00-03:00" ], "th": [], "fr": [], "sa": [], "su": [], "ph": [] } },
			{ "interval": 20, "applies": { "mo": [], "tu": [], "we": [], "th": [], "fr": [], "sa": [ "05:00-07:00" ], "su": [], "ph": [] } }
		]
		result = Main()._intervalConditionObjectToIntervalByDays(intvObj)
		expected = [
			{ "days": [ "mo" ], "intervals": { "00:00-01:00": 10 } },
			{ "days": [ "tu" ], "intervals": { "01:00-02:00": 10 } },
			{ "days": [ "we" ], "intervals": { "02:00-03:00": 10 } },
			{ "days": [ "sa" ], "intervals": { "05:00-07:00": 20 } }
		]
		self.assertEqual(result, expected)

	def test_intervalConditionObjectToIntervalByDays_merges_equal_days(self):
		intvObj = [
			{ "interval": 10, "applies": { "mo": [ "00:00-01:00" ], "tu": [ "00:00-01:00" ], "we": [ "00:00-01:00" ], "th": [], "fr": [], "sa": [], "su": [], "ph": [] } },
			{ "interval": 20, "applies": { "mo": [], "tu": [], "we": [], "th": [], "fr": [], "sa": [ "05:00-07:00" ], "su": [], "ph": [] } }
		]
		result = Main()._intervalConditionObjectToIntervalByDays(intvObj)
		expected = [
			{ "days": [ "mo", "tu", "we" ], "intervals": { "00:00-01:00": 10 } },
			{ "days": [ "sa" ], "intervals": { "05:00-07:00": 20 } }
		]
		self.assertEqual(result, expected)

	def test_intervalConditionObjectToIntervalByDays_distinguish_partially_equal_days(self):
		intvObj = [
			{ "interval": 10, "applies": { "mo": [ "00:00-01:00" ], "tu": [ "00:00-01:00", "05:00-07:00" ], "we": [ "00:00-01:00" ], "th": [], "fr": [], "sa": [], "su": [], "ph": [] } },
			{ "interval": 20, "applies": { "mo": [], "tu": [], "we": [], "th": [], "fr": [], "sa": [ "05:00-07:00" ], "su": [], "ph": [] } }
		]
		result = Main()._intervalConditionObjectToIntervalByDays(intvObj)
		expected = [
			{ "days": [ "mo", "we" ], "intervals": { "00:00-01:00": 10 } },
			{ "days": [ "tu" ], "intervals": { "00:00-01:00": 10, "05:00-07:00": 10 } },
			{ "days": [ "sa" ], "intervals": { "05:00-07:00": 20 } }
		]
		self.assertEqual(result, expected)

	#
	# _computeAllIntervals
	#

	def test_computeAllIntervals_works_all_data_set(self):
		interval = 10
		openingHours = {
			"mo": ["05:00-22:00"],
			"tu": ["05:00-22:00"],
			"we": ["05:00-22:00"],
			"th": ["05:00-22:00"],
			"fr": ["05:00-22:00"],
			"sa": ["07:00-23:00"],
			"su": [],
			"ph": []
		}
		intervalCondByDay = [
			{ "days": [ "mo", "tu", "we", "th", "fr" ], "intervals": { "08:00-10:00": 5, "16:30-18:30": 5 } },
			{ "days": [ "sa" ], "intervals": { "11:00-13:00": 6 } }
		]
		result = Main()._computeAllIntervals(openingHours, interval, intervalCondByDay)

		expected = [
			{ "days": [ "mo", "tu", "we", "th", "fr" ], "intervals": { "05:00-08:00": 10, "08:00-10:00": 5, "10:00-16:30": 10, "16:30-18:30": 5, "18:30-22:00": 10 } },
			{ "days": [ "sa" ], "intervals": { "07:00-11:00": 10, "11:00-13:00": 6, "13:00-23:00": 10 } }
		]

		self.assertEqual(result, expected)

	def test_computeAllIntervals_works_days_without_condinterval(self):
		interval = 10
		openingHours = {
			"mo": ["05:00-22:00"],
			"tu": ["05:00-22:00"],
			"we": ["05:00-22:00"],
			"th": ["05:00-22:00"],
			"fr": ["05:00-22:00"],
			"sa": ["07:00-23:00"],
			"su": [],
			"ph": []
		}
		intervalCondByDay = [
			{ "days": [ "mo", "fr" ], "intervals": { "08:00-10:00": 5, "16:30-18:30": 5 } },
			{ "days": [ "sa" ], "intervals": { "11:00-13:00": 6 } }
		]
		result = Main()._computeAllIntervals(openingHours, interval, intervalCondByDay)

		expected = [
			{ "days": [ "mo", "fr" ], "intervals": { "05:00-08:00": 10, "08:00-10:00": 5, "10:00-16:30": 10, "16:30-18:30": 5, "18:30-22:00": 10 } },
			{ "days": [ "tu", "we", "th" ], "intervals": { "05:00-22:00": 10 } },
			{ "days": [ "sa" ], "intervals": { "07:00-11:00": 10, "11:00-13:00": 6, "13:00-23:00": 10 } }
		]

		self.assertEqual(result, expected)

	def test_computeAllIntervals_works_sameoh_diffcondinterval(self):
		interval = 10
		openingHours = {
			"mo": ["05:00-22:00"],
			"tu": ["05:30-22:30"],
			"we": ["05:00-22:00"],
			"th": ["05:30-22:30"],
			"fr": ["05:00-22:00"],
			"sa": ["07:00-23:00"],
			"su": [],
			"ph": []
		}
		intervalCondByDay = [
			{ "days": [ "mo", "tu", "we", "th", "fr" ], "intervals": { "08:00-10:00": 5, "16:30-18:30": 5 } },
			{ "days": [ "sa" ], "intervals": { "11:00-13:00": 6 } }
		]
		result = Main()._computeAllIntervals(openingHours, interval, intervalCondByDay)

		expected = [
			{ "days": [ "mo", "we", "fr" ], "intervals": { "05:00-08:00": 10, "08:00-10:00": 5, "10:00-16:30": 10, "16:30-18:30": 5, "18:30-22:00": 10 } },
			{ "days": [ "tu", "th" ], "intervals": { "05:30-08:00": 10, "08:00-10:00": 5, "10:00-16:30": 10, "16:30-18:30": 5, "18:30-22:30": 10 } },
			{ "days": [ "sa" ], "intervals": { "07:00-11:00": 10, "11:00-13:00": 6, "13:00-23:00": 10 } }
		]

		self.assertEqual(result, expected)

	def test_computeAllIntervals_works_nocondinterval(self):
		interval = 10
		openingHours = {
			"mo": ["05:00-22:00"],
			"tu": ["05:00-22:00"],
			"we": ["05:00-22:00"],
			"th": ["05:00-22:00"],
			"fr": ["05:00-22:00"],
			"sa": ["07:00-23:00"],
			"su": [],
			"ph": []
		}
		intervalCondByDay = "unset"
		result = Main()._computeAllIntervals(openingHours, interval, intervalCondByDay)

		expected = [
			{ "days": [ "mo", "tu", "we", "th", "fr" ], "intervals": { "05:00-22:00": 10 } },
			{ "days": [ "sa" ], "intervals": { "07:00-23:00": 10 } }
		]

		self.assertEqual(result, expected)

	def test_computeAllIntervals_fail_if_novalid_condinterval(self):
		interval = 10
		openingHours = {
			"mo": ["05:00-22:00"],
			"tu": ["05:00-22:00"],
			"we": ["05:00-22:00"],
			"th": ["05:00-22:00"],
			"fr": ["05:00-22:00"],
			"sa": ["07:00-23:00"],
			"su": [],
			"ph": []
		}
		intervalCondByDay = "invalid"
		result = Main()._computeAllIntervals(openingHours, interval, intervalCondByDay)

		expected = "invalid"

		self.assertEqual(result, expected)

	def test_computeAllIntervals_works_if_oh_unset(self):
		interval = 10
		openingHours = "unset"
		intervalCondByDay = [
			{ "days": [ "mo", "tu", "we", "th", "fr" ], "intervals": { "08:00-10:00": 5, "16:30-18:30": 5 } },
			{ "days": [ "sa" ], "intervals": { "11:00-13:00": 6 } }
		]
		result = Main()._computeAllIntervals(openingHours, interval, intervalCondByDay)

		expected = [
			{ "days": [ "mo", "tu", "we", "th", "fr" ], "intervals": { "00:00-08:00": 10, "08:00-10:00": 5, "10:00-16:30": 10, "16:30-18:30": 5, "18:30-24:00": 10 } },
			{ "days": [ "sa" ], "intervals": { "00:00-11:00": 10, "11:00-13:00": 6, "13:00-24:00": 10 } },
			{ "days": [ "su", "ph" ], "intervals": { "00:00-24:00": 10 } }
		]

		self.assertEqual(result, expected)

	def test_computeAllIntervals_returns_only_condinterval_if_oh_invalid(self):
		interval = 10
		openingHours = "invalid"
		intervalCondByDay = [
			{ "days": [ "mo", "tu", "we", "th", "fr" ], "intervals": { "08:00-10:00": 5, "16:30-18:30": 5 } },
			{ "days": [ "sa" ], "intervals": { "11:00-13:00": 6 } }
		]
		result = Main()._computeAllIntervals(openingHours, interval, intervalCondByDay)

		expected = intervalCondByDay

		self.assertEqual(result, expected)

	def test_computeAllIntervals_returns_only_condinterval_if_interval_unset(self):
		interval = "unset"
		openingHours = {
			"mo": ["05:00-22:00"],
			"tu": ["05:00-22:00"],
			"we": ["05:00-22:00"],
			"th": ["05:00-22:00"],
			"fr": ["05:00-22:00"],
			"sa": ["07:00-23:00"],
			"su": [],
			"ph": []
		}
		intervalCondByDay = [
			{ "days": [ "mo", "tu", "we", "th", "fr" ], "intervals": { "08:00-10:00": 5, "16:30-18:30": 5 } },
			{ "days": [ "sa" ], "intervals": { "11:00-13:00": 6 } }
		]
		result = Main()._computeAllIntervals(openingHours, interval, intervalCondByDay)

		expected = intervalCondByDay

		self.assertEqual(result, expected)

	def test_computeAllIntervals_handles_oh_notcovering_condinterval(self):
		interval = 10
		openingHours = {
			"mo": ["05:00-12:00"],
			"tu": ["05:00-12:00"],
			"we": ["05:00-12:00"],
			"th": ["05:00-12:00"],
			"fr": ["05:00-12:00"],
			"sa": ["07:00-23:00"],
			"su": [],
			"ph": []
		}
		intervalCondByDay = [
			{ "days": [ "mo", "tu", "we", "th", "fr" ], "intervals": { "08:00-10:00": 5, "16:30-18:30": 5 } },
			{ "days": [ "sa" ], "intervals": { "11:00-13:00": 6 } }
		]

		self.assertRaises(Exception, Main()._computeAllIntervals, openingHours, interval, intervalCondByDay)

	def test_computeAllIntervals_handles_condinterval_startend_overlaps_oh(self):
		interval = 30
		openingHours = {
			"mo": ["05:00-22:00"],
			"tu": ["05:00-22:00"],
			"we": ["05:00-22:00"],
			"th": ["05:00-22:00"],
			"fr": ["05:00-22:00"],
			"sa": ["05:00-22:00"],
			"su": [],
			"ph": []
		}
		intervalCondByDay = [
			{ "days": [ "mo", "tu", "we", "th", "fr" ], "intervals": { "05:00-09:00": 15, "16:00-20:00": 15 } },
			{ "days": [ "sa" ], "intervals": { "05:00-10:00": 60, "20:00-22:00": 60 } }
		]
		result = Main()._computeAllIntervals(openingHours, interval, intervalCondByDay)

		expected = [
			{ "days": [ "mo", "tu", "we", "th", "fr" ], "intervals": { "05:00-09:00": 15, "09:00-16:00": 30, "16:00-20:00": 15, "20:00-22:00": 30 } },
			{ "days": [ "sa" ], "intervals": { "05:00-10:00": 60, "10:00-20:00": 30, "20:00-22:00": 60 } }
		]

		self.assertEqual(result, expected)

	#
	# _mergeIntervalsSingleDay
	#
	def test_mergeIntervalsSingleDay_works_1hour_range(self):
		ohRanges = ["03:00-22:30"]
		interval = 10
		condIntervals = { "07:00-09:30": 5, "18:00-20:25": 4 }

		result = Main()._mergeIntervalsSingleDay(ohRanges, interval, condIntervals)
		expected = { "03:00-07:00": 10, "07:00-09:30": 5, "09:30-18:00": 10, "18:00-20:25": 4, "20:25-22:30": 10 }

		self.assertEqual(result, expected)

	def test_mergeIntervalsSingleDay_works_multiple_hour_ranges(self):
		ohRanges = ["03:00-12:00", "15:00-23:50"]
		interval = 10
		condIntervals = { "07:00-09:30": 5, "18:00-20:25": 4 }

		result = Main()._mergeIntervalsSingleDay(ohRanges, interval, condIntervals)
		expected = { "03:00-07:00": 10, "07:00-09:30": 5, "09:30-12:00": 10, "15:00-18:00": 10, "18:00-20:25": 4, "20:25-23:50": 10 }

		self.assertEqual(result, expected)

	def test_mergeIntervalsSingleDay_fails_oh_notcovering_condintervals(self):
		ohRanges = ["03:00-15:15"]
		interval = 10
		condIntervals = { "07:00-09:30": 5, "18:00-20:25": 4 }

		self.assertRaises(Exception, Main()._mergeIntervalsSingleDay, ohRanges, interval, condIntervals)

	def test_mergeIntervalsSingleDay_fails_multiple_hour_ranges_notcovering_condinterval(self):
		ohRanges = ["03:00-12:00", "15:00-20:00"]
		interval = 10
		condIntervals = { "01:00-04:00": 12, "11:30-12:30": 5, "14:00-16:00": 4, "19:00-22:00": 3 }

		self.assertRaises(Exception, Main()._mergeIntervalsSingleDay, ohRanges, interval, condIntervals)

	def test_mergeIntervalsSingleDay_works_oh_equals_condintervals(self):
		ohRanges = ["07:00-09:30", "18:00-20:25"]
		interval = 10
		condIntervals = { "07:00-09:30": 5, "18:00-20:25": 4 }

		result = Main()._mergeIntervalsSingleDay(ohRanges, interval, condIntervals)
		expected = condIntervals

		self.assertEqual(result, expected)

	def test_mergeIntervalsSingleDay_works_condint_overlapping_start_oh(self):
		ohRanges = ["05:00-22:00"]
		interval = 30
		condIntervals = { "05:00-09:00": 15, "16:00-20:00": 15 }

		result = Main()._mergeIntervalsSingleDay(ohRanges, interval, condIntervals)
		expected = { "05:00-09:00": 15, "09:00-16:00": 30, "16:00-20:00": 15, "20:00-22:00": 30 }

		self.assertEqual(result, expected)

	def test_mergeIntervalsSingleDay_works_condint_overlapping_end_oh(self):
		ohRanges = ["05:00-22:00"]
		interval = 30
		condIntervals = { "05:30-09:00": 15, "16:00-22:00": 15 }

		result = Main()._mergeIntervalsSingleDay(ohRanges, interval, condIntervals)
		expected = { "05:00-05:30": 30, "05:30-09:00": 15, "09:00-16:00": 30, "16:00-22:00": 15 }

		self.assertEqual(result, expected)

	def test_mergeIntervalsSingleDay_works_condint_overlaps_startend_oh(self):
		ohRanges = ["05:00-22:00"]
		interval = 30
		condIntervals = { "05:00-09:00": 15, "16:00-22:00": 15 }

		result = Main()._mergeIntervalsSingleDay(ohRanges, interval, condIntervals)
		expected = { "05:00-09:00": 15, "09:00-16:00": 30, "16:00-22:00": 15 }

		self.assertEqual(result, expected)

	def test_mergeIntervalsSingleDay_works_condint_overlaps_startend_oh2(self):
		ohRanges = ["05:00-22:00"]
		interval = 30
		condIntervals = { "05:00-09:00": 15 }

		result = Main()._mergeIntervalsSingleDay(ohRanges, interval, condIntervals)
		expected = { "05:00-09:00": 15, "09:00-22:00": 30 }

		self.assertEqual(result, expected)

	#
	# intervalStringToMinutes
	#
	def test_intervalStringToMinutes_hhmmss1(self):
		interval = "01:00:00"
		result = Main().intervalStringToMinutes(interval)
		expected = 60
		self.assertEqual(result, expected)

	def test_intervalStringToMinutes_hhmmss2(self):
		interval = "01:30:00"
		result = Main().intervalStringToMinutes(interval)
		expected = 90
		self.assertEqual(result, expected)


	def test_intervalStringToMinutes_hhmmss3(self):
		interval = "02:45:30"
		result = Main().intervalStringToMinutes(interval)
		expected = 165.5
		self.assertEqual(result, expected)


	def test_intervalStringToMinutes_hhmm1(self):
		interval = "01:00"
		result = Main().intervalStringToMinutes(interval)
		expected = 60
		self.assertEqual(result, expected)


	def test_intervalStringToMinutes_hhmm2(self):
		interval = "03:12"
		result = Main().intervalStringToMinutes(interval)
		expected = 192
		self.assertEqual(result, expected)


	def test_intervalStringToMinutes_mm1(self):
		interval = "15"
		result = Main().intervalStringToMinutes(interval)
		expected = 15
		self.assertEqual(result, expected)


	def test_intervalStringToMinutes_mm2(self):
		interval = "135"
		result = Main().intervalStringToMinutes(interval)
		expected = 135
		self.assertEqual(result, expected)


	def test_intervalStringToMinutes_hmm(self):
		interval = "3:10"
		result = Main().intervalStringToMinutes(interval)
		expected = 190
		self.assertEqual(result, expected)


	def test_intervalStringToMinutes_invalid(self):
		interval = "12 minutes"
		self.assertRaises(Exception, Main().intervalStringToMinutes, interval)


if __name__ == '__main__':
	unittest.main()
