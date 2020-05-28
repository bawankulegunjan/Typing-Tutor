(defvar n)
(princ "Enter the number to find Factorial:")
(setq x (read))

(defun factorial (n)
	(if(= n 0)1
		(* n (factorial(- n 1)))))
  
(format t "~D! is ~D" x(factorial x))

