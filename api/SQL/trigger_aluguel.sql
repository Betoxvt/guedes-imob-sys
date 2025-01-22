CREATE TRIGGER tr_block_aluguel_conflict
ON alugueis
BEFORE INSERT
AS
BEGIN
    IF EXISTS (
        SELECT 1
        FROM alugueis a
        INNER JOIN inserted i ON a.apto_id = i.apto_id
        WHERE NOT (a.checkout <= i.checkin OR a.checkin >= i.checkout)
    )
    BEGIN
        RAISERROR('Apartamento já reservado para este período.', 16, 1)
        ROLLBACK TRANSACTION
        RETURN
    END
END