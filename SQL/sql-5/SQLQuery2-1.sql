/* ������� ������ ��������, ���� ��������� ���� �������������� ������������� � ��� ������ ��������� 100000 */

select Building, sum(Financing) as [��������� ����] from Department
group by Building
having sum(Financing) > 100000
