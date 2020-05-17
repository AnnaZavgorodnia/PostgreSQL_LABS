SELECT count(*) FROM (
	SELECT term FROM frequency
	WHERE count=1 AND docid IN ('10398_txt_earn', '925_txt_trade')
	GROUP BY term
);