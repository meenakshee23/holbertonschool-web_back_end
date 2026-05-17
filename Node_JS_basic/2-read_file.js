const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');

    const lines = data.split('\n').filter((line) => line);

    const students = lines.slice(1);

    console.log(`Number of students: ${students.length}`);

    const cs = [];
    const swe = [];

    students.forEach((student) => {
      const info = student.split(',');

      if (info[3] === 'CS') {
        cs.push(info[0]);
      } else if (info[3] === 'SWE') {
        swe.push(info[0]);
      }
    });

    console.log(`Number of students in CS: ${cs.length}. List: ${cs.join(', ')}`);
    console.log(`Number of students in SWE: ${swe.length}. List: ${swe.join(', ')}`);
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
