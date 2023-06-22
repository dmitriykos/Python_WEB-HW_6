-- 1 Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
SELECT s.fullname, ROUND(AVG(g.grade), 2) AS average_mark
FROM students AS s 
JOIN grades AS g ON g.student_id = s.id
GROUP BY s.id 
ORDER BY AVG(g.grade) DESC 
LIMIT 5;

-- 2 Знайти студента із найвищим середнім балом з певного предмета.
SELECT s.fullname, d.name, ROUND(AVG(g.grade), 2) AS average_mark
FROM grades AS g 
JOIN students AS s ON s.id = g.student_id 
JOIN disciplines AS d ON d.id = g.discipline_id 
WHERE d.id = 2
GROUP BY s.fullname, d.name
ORDER BY AVG(g.grade) DESC 
LIMIT 1;

-- 3 Знайти середній бал у групах з певного предмета.
SELECT g2.name, d.name, ROUND(AVG(g.grade), 2)
FROM grades g 
LEFT JOIN students AS s ON s.id  = g.student_id 
LEFT JOIN disciplines AS d ON d.id = g.discipline_id 
LEFT JOIN groups AS g2 ON g2.id = s.group_id
WHERE d.id = 1
GROUP BY g2.id, d.name
ORDER BY AVG(g.grade) DESC;

-- 4 Знайти середній бал на потоці (по всій таблиці оцінок).
SELECT ROUND(AVG(g.grade), 2) AS average_mark
FROM grades AS g;

-- 5 Знайти які курси читає певний викладач.
SELECT t.fullname, d.name  
FROM disciplines AS d 
LEFT JOIN teachers AS t ON t.id = d.teacher_id 
WHERE t.id = 2;

-- 6 Знайти список студентів у певній групі.
SELECT g.name, s.fullname
FROM students AS s
LEFT JOIN groups AS g ON g.id = s.group_id 
WHERE g.id = 1;

-- 7 Знайти оцінки студентів у окремій групі з певного предмета.
SELECT gr.name AS Group_Name, s.fullname AS student, d.name AS subject, g.grade AS mark
FROM grades AS g
LEFT JOIN students AS s ON s.id  = g.student_id 
JOIN disciplines AS d ON d.id = g.discipline_id 
LEFT JOIN groups AS gr ON gr.id = s.group_id
WHERE gr.id = 3 AND d.id = 3
ORDER BY s.fullname DESC;

-- 8 Знайти середній бал, який ставить певний викладач зі своїх предметів.
SELECT t.fullname  AS teacher , ROUND(AVG(g.grade),2) AS average_mark
FROM disciplines d 
LEFT JOIN grades g ON g.discipline_id = d.id 
LEFT JOIN teachers t ON t.id = d.teacher_id
WHERE t.id = 4
group by t.fullname;

-- 9 Знайти список курсів, які відвідує студент.
SELECT s.fullname AS student, d.name AS discipline
FROM grades AS g
LEFT JOIN students AS s ON s.id = g.student_id
LEFT JOIN disciplines AS d ON d.id = g.discipline_id
WHERE s.id = 9
GROUP BY d.id, s.fullname;

-- 10 Список курсів, які певному студенту читає певний викладач.
SELECT d.name AS subject, s.fullname AS student, t.fullname AS teacher 
FROM grades AS g 
LEFT JOIN disciplines AS d ON d.id = g.discipline_id 
LEFT JOIN teachers AS t ON t.id = g.discipline_id
LEFT JOIN students AS s ON s.id = g.student_id
WHERE s.id = 1 AND t.id = 3
GROUP BY d.id, s.fullname, t.fullname;

-- 11 Середній бал, який певний викладач ставить певному студентові.
SELECT t.fullname AS TEACHER, s.fullname AS STUDENT, ROUND(AVG(g.grade), 2) AS AVERAGE_MARK
FROM grades AS g
LEFT JOIN disciplines AS d ON d.id = g.discipline_id 
LEFT JOIN teachers AS t ON t.id = d.teacher_id 
LEFT JOIN students AS s ON s.id  = g.student_id
WHERE s.id = 4 AND t.id = 3
GROUP BY t.fullname, s.fullname;
