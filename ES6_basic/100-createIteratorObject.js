export default function createIteratorObject(report) {
  function* iterate() {
    for (const dept of Object.values(report.allEmployees)) {
      for (const employee of dept) {
        yield employee;
      }
    }
  }

  return iterate();
}
