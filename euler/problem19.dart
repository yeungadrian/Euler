void main() {
  print(calculateNumberOfSundays());
}

calculateNumberOfSundays() {
  int days = 1;

  List thirtyDays = [9, 4, 6, 11];

  List firstDayOfMonth = [days];

  for (var j = 0; j < 101; j++) {
    for (var i = 1; i < 13; i++) {
      if (i == 2) {
        if ((j % 4 == 0) & (j != 0)) {
          days += 29;
        } else {
          days += 28;
        }
      } else if (thirtyDays.contains(i)) {
        days += 30;
      } else {
        days += 31;
      }
      ;
      firstDayOfMonth.add(days);
    }
  }

  List sundays =
      firstDayOfMonth.where((i) => (i % 7 == 0) & (i > 365)).toList();

  return (sundays.length);
}
