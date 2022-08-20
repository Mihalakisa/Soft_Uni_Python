from unittest import TestCase
from project.team import Team


class TeamTest(TestCase):
    def setUp(self) -> None:
        self.team = Team('Team')

    def test_team_init(self):
        self.team = Team('Team')
        self.assertEqual(self.team.name, 'Team')
        self.assertEqual({}, self.team.members)

    def test_name_error_if_alpha(self):
        with self.assertRaises(ValueError) as error:
            self.team = Team('1x')
        self.assertEqual("Team Name can contain only letters!", str(error.exception))

    def test_add_member_only_new_players_to_the_team(self):
        self.team.members['Ivan'] = 18

        result = self.team.add_member(Ivan=22, Pesho=18, Gosho=20, Josh=16)

        self.assertEqual(f"Successfully added: Pesho, Gosho, Josh", result)
        self.assertEqual(18, self.team.members['Pesho'])
        self.assertEqual(20, self.team.members['Gosho'])
        self.assertEqual(16, self.team.members['Josh'])

    def test_remove_member_who_not_exists(self):
        result = self.team.remove_member('Batman')
        self.assertEqual("Member with name Batman does not exist", result)

    def test_remove_member_who_exists(self):
        self.team.members['Ivan'] = 18
        self.team.members['Pesho'] = 19
        result = self.team.remove_member('Ivan')
        self.assertEqual("Member Ivan removed", result)
        self.assertEqual(19, self.team.members['Pesho'])
        self.assertTrue('Ivan' not in self.team.members)

    def test_gt_compares_team_by_members_count(self):
        self.team.members['member1'] = 18
        self.team.members['member2'] = 19

        another_team = Team('Another')
        another_team.members['member1'] = 21
        another_team.members['member2'] = 22
        another_team.members['member3'] = 23

        self.assertEqual(True, another_team > self.team)
        self.assertEqual(False, another_team < self.team)

    def test_len_returns_members_count(self):
        self.team.members['member1'] = 18
        self.team.members['member2'] = 19

        self.assertEqual(2, len(self.team))

    def test_add_returns_new_team_with_combined_members(self):
        self.team.members['member1'] = 18
        self.team.members['member2'] = 19

        another_team = Team('Another')
        another_team.members['member3'] = 21
        another_team.members['member4'] = 22
        another_team.members['member5'] = 23

        result = self.team + another_team
        expected_result_members = {
            'member1': 18,
            'member2': 19,
            'member3': 21,
            'member4': 22,
            'member5': 23
        }

        self.assertEqual('TeamAnother', result.name)
        self.assertEqual(expected_result_members, result.members)

    def test_str_returns_members_sorted_in_descending_order_by_age_in_proper_string_format(self):
        self.team.members['member2'] = 19
        self.team.members['member1'] = 18
        self.team.members['member3'] = 20

        result = str(self.team)
        expected = f"Team name: Team\n" + \
            f"Member: member3 - 20-years old\n" + \
            f"Member: member2 - 19-years old\n" + \
            f"Member: member1 - 18-years old"

        self.assertEqual(expected, result)