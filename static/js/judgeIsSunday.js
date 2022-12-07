function judgeIsSunday(year, month, day) {
    const date = new Date(year=year, month=month - 1, day=day)
    return date.getDay() == 0
}