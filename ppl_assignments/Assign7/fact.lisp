(defvar n)
(defvar ans)
(defvar x)
(defun factorial ()
  (princ "Enter the number to find Factorial:")
  (setq n (read))
  (setq ans 1)
  (loop for x from 1 to n
	do(setq ans (* ans x))
  )
  (write  ans )
 )
(factorial)

