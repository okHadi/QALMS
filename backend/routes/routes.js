import { Router } from "express";
const router = Router();

router.get('/', async (req, res) => {
    try {
        res.json({ "message": "QALMS ROUTES!" });
    }
    catch (error) { res.status(500).json({ message: "" + error }); }
});


export default router;